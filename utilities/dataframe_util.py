from typing import Type, List
from datetime import datetime
import pandas as pd
from pandas import DataFrame
from utilities.configurator import Configurator
from warnings import simplefilter
from dateutil.parser import parse

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
        self.now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

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

    def union_dataframes(self) -> DataFrame:
        print("Concatenating Dataframes")
        dataframe = pd.concat(self.cleaned_dataframes)
        return self.clean_dataframe(dataframe)

    def clean_dataframe(self, dataframe: pd.DataFrame) -> DataFrame:
        dataframe.columns = map(str.lower, dataframe.columns)
        dataframe[self.div] = self.configs.file_name
        dataframe = dataframe.loc[:, ~dataframe.columns.str.startswith("unnamed")]
        dataframe = dataframe.loc[:, ~dataframe.columns.str.startswith("Unnamed")]
        dataframe = dataframe.replace("#", None)

        """
        Unfortunately the people who curate this data think having four different timestamps 
        is the way to go... maybe this will go away if I decide to convert to a spark 
        application but doubt it. (pain)
        """
        dataframe_us_full_year = pd.to_datetime(dataframe["date"], format="%m/%d/%Y", errors='coerce')
        dataframe_eu_full_year = pd.to_datetime(dataframe["date"], format="%d/%m/%Y", errors='coerce')
        dataframe_us_half_year = pd.to_datetime(dataframe["date"], format="%m/%d/%y", errors='coerce')
        dataframe_eu_half_year = pd.to_datetime(dataframe["date"], format="%d/%m/%y", errors='coerce')
        final_dataframe = dataframe.copy()
        final_dataframe["date"] = dataframe_eu_full_year.fillna(dataframe_us_full_year).fillna(dataframe_eu_half_year).fillna(
            dataframe_us_half_year)

        return self.add_high_watermark(final_dataframe)

    def add_high_watermark(self, dataframe: pd.DataFrame) -> DataFrame:
        dataframe["high_water_mark"] = self.now
        return dataframe

    @staticmethod
    def high_water_mark_filter(dataframe: pd.DataFrame, previous_time_stamp: str) -> DataFrame:
        dataframe = dataframe[dataframe.date > previous_time_stamp]
        return dataframe

    @staticmethod
    def add_columns(dataframe: DataFrame, cols_to_add: List[str]):
        dataframe[cols_to_add] = None
        return dataframe
