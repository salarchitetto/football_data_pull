from configs import LeagueDictionary
from postgres.postgres_utils import PostgresUtils
from utilities.configurator import Configurator
from utilities.dataframe_util import DataframeUtil
from utilities.logger import Logger
from utilities.season_dates import SeasonDates


class ProcessorBackFill:
    def __init__(self,
                 configs: Configurator, table_name: str):
        self.configs = configs
        self.table_name = table_name
        self.checks = [LeagueDictionary.SERIEB.name.lower(),
                       LeagueDictionary.LALIGA2.name.lower(),
                       LeagueDictionary.SCOT_PREM.name.lower()]

    def process_back_fill(self) -> None:
        logger = Logger(logger_name="Data Backfill Processor")

        dataframe_util = DataframeUtil(self.configs)
        download_paths = SeasonDates(self.configs).get_multiple_season_download_paths()

        dataframes = dataframe_util.create_dataframe_list(download_paths)
        columns = dataframe_util.find_all_column_names(dataframes)
        cleaned_dataframes = dataframe_util.add_missing_columns_to_dataframe(columns, dataframes)

        if self.configs.file_name == LeagueDictionary.PREMIER_LEAGUE.name.lower():
            dataframe = dataframe_util.union_dataframes(cleaned_dataframes)
            PostgresUtils().create_table_from_existing_dataframe(dataframe, self.table_name)
            PostgresUtils().upload_dataframe(dataframe, self.table_name)

        elif self.configs.file_name in self.checks:
            for dataframe in cleaned_dataframes:
                dataframe = dataframe_util.clean_dataframe(dataframe)
                cols_to_add = self.configs.find_diff_between_lists(PostgresUtils()
                                                                   .grab_table_schema(self.table_name),
                                                                   dataframe.columns)
                dataframe = dataframe_util.add_columns(dataframe, cols_to_add)
                PostgresUtils().upload_dataframe(dataframe[PostgresUtils()
                                                 .grab_table_schema(self.table_name)], self.table_name)

        else:
            dataframe = dataframe_util.union_dataframes(dataframes)
            cols_to_add = self.configs.find_diff_between_lists\
                (PostgresUtils().grab_table_schema(self.table_name), dataframe.columns)
            dataframe = dataframe_util.add_columns(dataframe, cols_to_add)
            PostgresUtils().upload_dataframe(dataframe[PostgresUtils()
                                             .grab_table_schema(self.table_name)], self.table_name)
