from configs import LeagueDictionary
from postgres.postgres_utils import PostgresUtils
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

    def process_back_fill(self, id_generator: TeamIDGenerator) -> None:
        dataframe_util = DataframeUtil(id_generator)
        column_util = ColumnUtils()
        download_paths = SeasonDates(self.configs).get_multiple_season_download_paths()

        dataframes = dataframe_util.create_dataframe_list(download_paths)
        columns = column_util.find_all_column_names(dataframes)
        cleaned_dataframes = column_util.add_missing_columns_to_dataframe(columns, dataframes)

        # TODO: refactor this
        if self.configs.file_name == LeagueDictionary.PREMIER_LEAGUE.name.lower():
            dataframe = dataframe_util.union_dataframes(cleaned_dataframes, self.configs.league_name)
            PostgresUtils().create_table_from_existing_dataframe(dataframe)
            PostgresUtils().upload_dataframe(dataframe)

        elif self.configs.file_name in self.checks:
            for dataframe in cleaned_dataframes:
                dataframe = dataframe_util.clean_dataframe(dataframe, self.configs.league_name)
                cols_to_add = self.configs.find_diff_between_lists(PostgresUtils().grab_table_schema(), dataframe.columns)
                dataframe = column_util.add_columns(dataframe, cols_to_add)
                PostgresUtils().upload_dataframe(dataframe[PostgresUtils().grab_table_schema()])

        else:
            dataframe = dataframe_util.union_dataframes(dataframes, self.configs.league_name)
            cols_to_add = self.configs.find_diff_between_lists(PostgresUtils().grab_table_schema(), dataframe.columns)
            dataframe = column_util.add_columns(dataframe, cols_to_add)
            PostgresUtils().upload_dataframe(dataframe[PostgresUtils().grab_table_schema()])
