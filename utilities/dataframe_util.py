from typing import List
from datetime import datetime
import pandas as pd
from pandas import DataFrame
from utilities.configurator import Configurator
from warnings import simplefilter

from utilities.logger import Logger

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


class DataframeUtil:
    def __init__(self, configs: Configurator = None):
        self.configs = configs
        self.division = "division"
        self.string_columns = ["Div", "Date", "Time", "HomeTeam", "AwayTeam", "FTR", "HTR"]
        self.now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.logger = Logger(logger_name="DataframeUtil")

    @staticmethod
    def get_dataframe(path) -> pd.DataFrame:
        return pd.read_csv(path, encoding='windows-1252', on_bad_lines='skip')

    @staticmethod
    def find_all_column_names(dataframes: List[DataFrame]) -> set[str]:
        cols = []
        for dataframe in dataframes:
            for columns in dataframe.columns:
                cols.append(columns)

        return set(cols)

    @staticmethod
    def add_missing_columns_to_dataframe(columns: set[str], dataframes: List[DataFrame]) -> List[DataFrame]:
        cleaned_dataframes = []
        for dataframe in dataframes:
            missing_columns = columns.difference(set(dataframe.columns.values))
            dataframe[list(missing_columns)] = None
            cleaned_dataframes.append(dataframe)

        return cleaned_dataframes

    def create_dataframe_list(self, paths: List[str]) -> List[DataFrame]:
        return [self.get_dataframe(path) for path in paths]

    def union_dataframes(self, dataframes: List[DataFrame]) -> DataFrame:
        self.logger.info("Concatenating Dataframes")
        dataframe = pd.concat(dataframes)
        return self.clean_dataframe(dataframe)

    @staticmethod
    def get_lowercase_columns(dataframe: pd.DataFrame) -> map:
        return map(str.lower, dataframe.columns)

    def convert_div_name(self, dataframe: pd.DataFrame) -> DataFrame:
        dataframe = dataframe.rename({"div": "division"})
        dataframe[self.division] = self.configs.league_name
        return dataframe

    def remove_col_name_string_starts_with(self, dataframe: pd.DataFrame, col_name: str) -> DataFrame:
        dataframe.columns = self.get_lowercase_columns(dataframe)
        return dataframe.loc[:, ~dataframe.columns.str.startswith(col_name)]

    @staticmethod
    def replace_values_in_dataframe(dataframe: pd.DataFrame, value_to_replace: str) -> DataFrame:
        return dataframe.replace(value_to_replace, None)

    @staticmethod
    def dataframe_datetime_polisher(dataframe: pd.DataFrame) -> DataFrame:
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
        final_dataframe["date"] = dataframe_eu_full_year\
            .fillna(dataframe_us_full_year)\
            .fillna(dataframe_eu_half_year)\
            .fillna(dataframe_us_half_year)

        return final_dataframe

    def clean_dataframe(self, dataframe: pd.DataFrame) -> DataFrame:
        dataframe = self.convert_div_name(dataframe)
        dataframe = self.remove_col_name_string_starts_with(dataframe, "unnamed")
        dataframe = self.replace_values_in_dataframe(dataframe, "#")
        final_dataframe = self.dataframe_datetime_polisher(dataframe)

        return self.add_high_watermark(final_dataframe)

    def add_high_watermark(self, dataframe: pd.DataFrame) -> DataFrame:
        dataframe["high_water_mark"] = self.now
        return dataframe

    def grab_dtypes(self, dataframe: pd.DataFrame) -> List[str]:

        dtypes = []
        for keys, values in dataframe.dtypes.items():
            dtypes.append(values.name)

        return self.type_checker(dtypes)

    def high_water_mark_filter(self, dataframe: pd.DataFrame, previous_time_stamp: str) -> DataFrame:
        self.logger.info(f"Previous timestamp: {previous_time_stamp}")
        dataframe = dataframe[dataframe["date"] > previous_time_stamp]
        return dataframe

    @staticmethod
    def add_columns(dataframe: DataFrame, cols_to_add: List[str]):
        dataframe[cols_to_add] = None
        return dataframe

    @staticmethod
    def type_checker(dtype_list: List[str]) -> List[str]:
        return list(map(lambda x: x.
                        replace("object", "text")
                        .replace("float64", "float")
                        .replace("int64", "integer")
                        .replace("datetime64[ns]", "timestamp"),
                        dtype_list))

    @staticmethod
    def remove_unnamed_from_column_name(dataframe: pd.DataFrame) -> pd.DataFrame:
        return dataframe.loc[:, ~dataframe.columns.str.startswith("Unnamed")]
