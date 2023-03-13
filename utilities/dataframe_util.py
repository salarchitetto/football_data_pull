import csv
from typing import Type, List

import pandas as pd
from pandas import DataFrame

from utilities.configurator import Configurator
from warnings import simplefilter

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


class DataframeUtil:
    def __init__(self, configs: Configurator = None):
        self.configs = configs
        self.dataframes = []
        self.columns = set()
        self.cleaned_dataframes = []
        self.debug = []
        self.div = "div"
        self.string_columns = ["Div", "Date", "Time", "HomeTeam", "AwayTeam", "FTR", "HTR"]


    @staticmethod
    def get_dataframe(path) -> pd.DataFrame:
        return pd.read_csv(path, encoding='windows-1252', on_bad_lines='skip')

    def save_dataframe(self, dataframe, csv_name: str) -> None:
        print(f"Saving Dataframe to path: {self.configs.get_directory}/{csv_name}")
        print(dataframe.columns)
        dataframe.to_csv(f"{self.configs.get_directory}/{csv_name}")

    def find_all_column_names(self) -> None:
        for dataframes in self.dataframes:
            for columns in dataframes.columns:
                self.columns.add(columns)

    def add_missing_columns_to_dataframe(self, dataframe: pd.DataFrame) -> None:

        missing_columns = self.columns.difference(set(dataframe.columns.values))
        print(f"Missing Columns for dataframe: {missing_columns}")

        dataframe[list(missing_columns)] = None
        self.cleaned_dataframes.append(dataframe)

    def append_dataframe_to_list(self, path: str) -> None:
        self.dataframes.append(self.get_dataframe(path))

    def union_dataframes(self) -> Type[DataFrame]:
        print("Concatenating Dataframes")
        dataframe = pd.concat(self.cleaned_dataframes)
        return self.clean_dataframe(dataframe)

    def clean_dataframe(self, dataframe: pd.DataFrame) -> Type[DataFrame]:
        dataframe.columns = map(str.lower, dataframe.columns)
        dataframe[self.div] = self.configs.file_name
        dataframe = dataframe.loc[:, ~dataframe.columns.str.startswith("unnamed")]
        dataframe = dataframe.loc[:, ~dataframe.columns.str.startswith("Unnamed")]
        dataframe = dataframe.replace("#", None)

        return dataframe

    @staticmethod
    def add_columns(dataframe: Type[DataFrame], cols_to_add: List[str]):
        dataframe[cols_to_add] = None
        return dataframe

