from configs import LeagueDictionary
from utilities.postgres.postgres_utils import PostgresUtils
from utilities.configurator import Configurator
from utilities.dataframe_util import DataframeUtil, ColumnUtils
from utilities.id_generator import TeamIDGenerator
from utilities.season_dates import SeasonDates


class ProcessorBackFill:
    def __init__(self,
                 configs: Configurator):
        self.configs = configs
        self.checks = [LeagueDictionary.SERIEB.name.lower(),
                       LeagueDictionary.LALIGA2.name.lower(),
                       LeagueDictionary.SCOT_PREM.name.lower()]
        self.season_dates = SeasonDates(configs)
        self.postgres_utils = PostgresUtils()

    def process_back_fill(self, id_generator: TeamIDGenerator) -> None:
        dataframe_util = DataframeUtil(id_generator)
        column_util = ColumnUtils()
        download_paths = self.season_dates.get_multiple_season_download_paths()
        formatted_season_list = self.season_dates.get_formatted_seasons_list()

        dataframes = dataframe_util.create_dataframe_list(download_paths)
        all_column_names = column_util.find_all_column_names(dataframes)
        final_dataframes = column_util.add_missing_columns_to_dataframe(all_column_names, dataframes)

        for index, (dataframe, season) in enumerate(zip(final_dataframes, formatted_season_list)):
            cleaned_dataframe = dataframe_util.clean_dataframe(dataframe, self.configs.league_name)
            dataframe_with_season = dataframe_util.add_season_to_dataframe(season, cleaned_dataframe)

            if self.configs.league_name == "premier_league" and index == 0:
                PostgresUtils().create_table_from_existing_dataframe(dataframe_with_season)

            cols_to_add = self.configs.find_diff_between_lists(PostgresUtils().grab_table_schema(),
                                                               cleaned_dataframe.columns)
            dataframe_with_missing_columns = column_util.add_columns(cleaned_dataframe, cols_to_add)
            self.postgres_utils.upload_dataframe(
                dataframe=dataframe_with_missing_columns[PostgresUtils().grab_table_schema()],
                msg=f"{self.configs.league_name} : {season}"
            )
