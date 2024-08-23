from datetime import datetime
from typing import List, Final, Dict, Optional

import polars as pl

from configuration.configuration_enums import SourceType
from configuration.football_data_uk_configuration import FOOTBALL_DATA_UK_MAPPING


class DataFrameUtilities:
    """
    A utility class for performing various operations on Polars DataFrames.

    TODO: Should this even be a class? Feels like it should just be functions,
        think about this some more. Everything in here is needed to be clean in
        the eyes of footydash

    Attributes:
        source_type (SourceType): The type of source for the DataFrame (e.g., Excel, CSV).
        path (str): The file path to the data source.
        current_timestamp (str): The current timestamp.
        DATE (str): The column name for date.
        HOME_TEAM (str): The column name for home team.
        AWAY_TEAM (str): The column name for away team.
    """

    def __init__(self, source_type: Optional[SourceType] = None, path: Optional[str] = None) -> None:
        """
        Initialize the DataFrameUtilities with optional source type and path.

        :param source_type: The type of source for the DataFrame (e.g., Excel, CSV).
        :param path: The file path to the data source.
        """
        self.source_type = source_type
        self.path = path
        self.current_timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.DATE: Final[str] = "date"
        self.HOME_TEAM: Final[str] = "home_team"
        self.AWAY_TEAM: Final[str] = "away_team"

    @property
    def source_type(self) -> Optional[SourceType]:
        """
        Get the source type of the DataFrame.

        :return: The source type.
        """
        return self._source_type

    @source_type.setter
    def source_type(self, value: SourceType) -> None:
        """
        Set the source type of the DataFrame.

        :param value: The source type to set.
        :raises AssertionError: If the value is not an instance of SourceType.
        """
        assert isinstance(value, SourceType), "Must be a valid source type"
        self._source_type = value

    @property
    def path(self) -> Optional[str]:
        """
        Get the file path to the data source.

        :return: The file path.
        """
        return self._path

    @path.setter
    def path(self, value: str) -> None:
        """
        Set the file path to the data source.

        :param value: The file path to set.
        :raises AssertionError: If the value is not a string.
        """
        assert isinstance(value, str), "Path must be a string"
        self._path = value

    def read_csv(self, path: Optional[str] = None) -> pl.DataFrame:
        """
        Read a CSV file into a Polars DataFrame.

        :param path: The file path to the CSV. If not provided, uses the instance's path attribute.
        :return: A Polars DataFrame.
        """
        if path:
            path_to_csv = path
        else:
            path_to_csv = self.path

        return pl.read_csv(path_to_csv, ignore_errors=True, try_parse_dates=True, truncate_ragged_lines=True)

    def clean_dataframe_depending_on_source_type(self) -> pl.DataFrame:
        """
        Clean the DataFrame based on the source type.

        :return: A cleaned Polars DataFrame.
        :raises ValueError: If source type is not specified or not supported.
        """
        if self.source_type == SourceType.EXCEL and self.path:
            dataframe_to_clean = (
                self.read_csv(self.path)
                .pipe(self.rename_multiple_column_names, FOOTBALL_DATA_UK_MAPPING)
                .pipe(self.convert_unformatted_dates, self.DATE, "%y-%m-%d")
                .pipe(self.clean_team_names, [self.HOME_TEAM, self.AWAY_TEAM])
                .pipe(self.select_columns_that_exist, FOOTBALL_DATA_UK_MAPPING)
            )
        else:
            raise ValueError("Source type must be either Excel or CSV, or it has not been implemented yet.")

        return dataframe_to_clean

    @classmethod
    def add_new_static_column(cls, dataframe: pl.DataFrame, new_column_name: str, static_value: str) -> pl.DataFrame:
        """
        Add a new column with a static value to the DataFrame.

        :param dataframe: The Polars DataFrame.
        :param new_column_name: The name of the new column.
        :param static_value: The static value to assign to the new column.
        :return: The updated DataFrame with the new column.
        """
        return dataframe.with_columns(pl.lit(static_value).alias(new_column_name))

    @classmethod
    def convert_column_name(cls, dataframe: pl.DataFrame, new_column_name: str, old_column_name: str) -> pl.DataFrame:
        """
        Rename a column in the DataFrame.

        :param dataframe: The Polars DataFrame.
        :param new_column_name: The new column name.
        :param old_column_name: The current column name to be renamed.
        :return: The DataFrame with the column renamed.
        """
        return dataframe.rename({old_column_name: new_column_name})

    @classmethod
    def rename_multiple_column_names(cls, dataframe: pl.DataFrame, columns_to_rename: Dict[str, str]) -> pl.DataFrame:
        """
        Rename multiple columns in the DataFrame based on a mapping dictionary.

        :param dataframe: The Polars DataFrame.
        :param columns_to_rename: A dictionary mapping old column names to new column names.
        :return: The DataFrame with columns renamed.
        """
        current_columns = dataframe.columns
        filtered_columns_to_rename = {col: new_name for col, new_name in columns_to_rename.items() if col in current_columns}
        return dataframe.rename(filtered_columns_to_rename)

    @classmethod
    def select_columns_that_exist(cls, dataframe: pl.DataFrame, columns_to_select: Dict[str, str]) -> pl.DataFrame:
        """
        Select columns that exist in the DataFrame based on a dictionary of column names.

        :param dataframe: The Polars DataFrame.
        :param columns_to_select: A dictionary of columns to select.
        :return: The DataFrame with only the selected columns.
        """
        current_columns = dataframe.columns
        filtered_columns_to_select = [col for col in columns_to_select.values() if col in current_columns]
        return dataframe.select(filtered_columns_to_select)

    @classmethod
    def convert_unformatted_dates(cls, dataframe: pl.DataFrame, date_column: str, new_format: str) -> pl.DataFrame:
        """
        Convert a date column to a different format.

        :param dataframe: The Polars DataFrame.
        :param date_column: The name of the date column to be reformatted.
        :param new_format: The desired date format.
        :return: A new Polars DataFrame with the date column reformatted.
        """
        return (
            dataframe
            .with_columns(
                pl.col(date_column)
                .dt.strftime(new_format)
                .alias(date_column)
            )
            .with_columns(
                pl.col(date_column)
                .str.to_date(format="%y-%m-%d")
                .alias(date_column)
            )
        )

    @classmethod
    def clean_team_names(cls, dataframe: pl.DataFrame, column_names: List[str]) -> pl.DataFrame:
        """
        Clean team names by replacing spaces with underscores and converting to lowercase.

        :param dataframe: The Polars DataFrame.
        :param column_names: A list of column names containing team names.
        :return: The DataFrame with cleaned team names.
        """
        return (
            dataframe
            .with_columns(
                [
                    pl.col(column)
                    .str.replace(" ", "_")
                    .str.to_lowercase()
                    .alias(column)
                    for column in column_names
                ]
            )
        )