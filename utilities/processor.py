from postgres.postgres_utils import PostgresUtils
from utilities.configurator import Configurator
import pandas as pd
from utilities.dataframe_util import DataframeUtil


class Processor:
    def __init__(self,
                 configs: Configurator,
                 dataframe_util: DataframeUtil):
        self.configs = configs
        self.dataframe_util = dataframe_util
        self.dataframes = []

    def process(self) -> None:
        self.configs.create_years_list()
        self.configs.list_checker()
        self.configs.create_csv_names()
        download_paths = self.configs.link_to_download_path()
        print(download_paths)

        for path, csv_name in zip(download_paths, self.configs.csv_names):
            print(f"Appending dataframe to list: {path}")
            self.dataframe_util.append_dataframe_to_list(path)

        self.dataframe_util.find_all_column_names()
        for dataframe in self.dataframe_util.dataframes:
            self.dataframe_util.add_missing_columns_to_dataframe(dataframe)

        if self.configs.league_name == "premier_league":
            dataframe = self.dataframe_util.union_dataframes()
            PostgresUtils().create_team_outcomes_table(dataframe)
            PostgresUtils().upload_dataframe(dataframe)
            self.dataframe_util.save_dataframe(dataframe, f"{self.configs.file_name}.csv")

        elif self.configs.league_name in ["scot_prem", "serieb", "laliga2"]:
            for dataframe in self.dataframe_util.cleaned_dataframes:
                dataframe = self.dataframe_util.clean_dataframe(dataframe)
                cols_to_add = self.configs.find_diff_between_lists(PostgresUtils().grab_results_schema(),
                                                                   dataframe.columns)
                dataframe = self.dataframe_util.add_columns(dataframe, cols_to_add)
                PostgresUtils().create_team_outcomes_table(dataframe)
                PostgresUtils().upload_dataframe(dataframe[PostgresUtils().grab_results_schema()])

        else:
            dataframe = self.dataframe_util.union_dataframes()
            PostgresUtils().create_team_outcomes_table(dataframe)
            cols_to_add = self.configs.find_diff_between_lists(PostgresUtils().grab_results_schema(), dataframe.columns)
            dataframe = self.dataframe_util.add_columns(dataframe, cols_to_add)
            PostgresUtils().upload_dataframe(dataframe[PostgresUtils().grab_results_schema()])

            self.dataframe_util.save_dataframe(dataframe, f"{self.configs.file_name}.csv")






