"""Polars Dataframe Methods."""

from datetime import datetime
from typing import Dict, List

import polars as pl
from polars import col, lit

from configuration.configuration_enums import Leagues, SourceType
from configuration.football_data_uk_configuration import FOOTBALL_DATA_UK_MAPPING
from utilities.logger import Logger

logger: Logger = Logger("FootyDataframes")


def dataframe_cleanser(
    source_type: SourceType, path: str, league_name: Leagues, season: str
) -> pl.DataFrame:
    """
    Clean the DataFrame based on the source type.

    :return: A cleaned Polars DataFrame.
    :raises ValueError: If source type is not specified or not supported.
    """
    if source_type == SourceType.EXCEL and path:
        dataframe_to_clean = (
            read_csv(path)
            .pipe(rename_multiple_column_names, FOOTBALL_DATA_UK_MAPPING)
            .pipe(convert_unformatted_dates, "date", "%y-%m-%d")
            .pipe(clean_team_names, ["home_team", "away_team"])
            .pipe(select_columns_that_exist, FOOTBALL_DATA_UK_MAPPING)
            .pipe(add_missing_columns, FOOTBALL_DATA_UK_MAPPING)
            .pipe(add_new_static_column, "high_water_mark", datetime.now())
            .pipe(add_new_static_column, "league_name", league_name.name.lower())
            .pipe(add_new_static_column, "season", season)
            .filter(col("date").is_not_null())
        )
        logger.info(f"Cleaning up provided dataframe via: {SourceType.EXCEL} | {path}")
    else:
        raise ValueError(
            "Source type must be either Excel or CSV, or it has not been implemented yet."
        )

    return dataframe_to_clean


def read_csv(path: str) -> pl.DataFrame:
    """
    Read a CSV file into a Polars DataFrame.

    :param path: The file path to the CSV. If not provided, uses the instance's path attribute.
    :return: A Polars DataFrame.
    """
    return pl.read_csv(
        path, ignore_errors=True, try_parse_dates=True, truncate_ragged_lines=True
    )


def add_new_static_column(
    dataframe: pl.DataFrame, new_column_name: str, static_value: str
) -> pl.DataFrame:
    """
    Add a new column with a static value to the DataFrame.

    :param dataframe: The Polars DataFrame.
    :param new_column_name: The name of the new column.
    :param static_value: The static value to assign to the new column.
    :return: The updated DataFrame with the new column.
    """
    return dataframe.with_columns(pl.lit(static_value).alias(new_column_name))


def convert_column_name(
    dataframe: pl.DataFrame, new_column_name: str, old_column_name: str
) -> pl.DataFrame:
    """
    Rename a column in the DataFrame.

    :param dataframe: The Polars DataFrame.
    :param new_column_name: The new column name.
    :param old_column_name: The current column name to be renamed.
    :return: The DataFrame with the column renamed.
    """
    return dataframe.rename({old_column_name: new_column_name})


def rename_multiple_column_names(
    dataframe: pl.DataFrame, columns_to_rename: Dict[str, str]
) -> pl.DataFrame:
    """
    Rename multiple columns in the DataFrame based on a mapping dictionary.

    :param dataframe: The Polars DataFrame.
    :param columns_to_rename: A dictionary mapping old column names to new column names.
    :return: The DataFrame with columns renamed.
    """
    current_columns = dataframe.columns
    filtered_columns_to_rename = {
        col: new_name["mapped_column_name"]
        for col, new_name in columns_to_rename.items()
        if col in current_columns
    }
    return dataframe.rename(filtered_columns_to_rename)


def select_columns_that_exist(
    dataframe: pl.DataFrame, columns_to_select: Dict[str, str]
) -> pl.DataFrame:
    """
    Select columns that exist in the DataFrame based on a dictionary of column names.

    :param dataframe: The Polars DataFrame.
    :param columns_to_select: A dictionary of columns to select.
    :return: The DataFrame with only the selected columns.
    """
    current_columns = dataframe.columns
    filtered_columns_to_select = [
        col["mapped_column_name"]
        for col in columns_to_select.values()
        if col["mapped_column_name"] in current_columns
    ]

    return dataframe.select(filtered_columns_to_select)


def convert_unformatted_dates(
    dataframe: pl.DataFrame, date_column: str, new_format: str
) -> pl.DataFrame:
    """
    Convert a date column to a different format.

    :param dataframe: The Polars DataFrame.
    :param date_column: The name of the date column to be reformatted.
    :param new_format: The desired date format.
    :return: A new Polars DataFrame with the date column reformatted.
    """
    return dataframe.with_columns(
        pl.col(date_column).dt.strftime(new_format).alias(date_column)
    ).with_columns(
        pl.col(date_column).str.to_date(format="%y-%m-%d").alias(date_column)
    )


def clean_team_names(dataframe: pl.DataFrame, column_names: List[str]) -> pl.DataFrame:
    """
    Clean team names by replacing spaces with underscores and converting to lowercase.

    :param dataframe: The Polars DataFrame.
    :param column_names: A list of column names containing team names.
    :return: The DataFrame with cleaned team names.
    """
    return dataframe.with_columns(
        [
            pl.col(column)
            .str.replace(" ", "_")
            .str.replace("'", "`")
            .str.to_lowercase()
            .alias(column)
            for column in column_names
        ]
    )


def add_missing_columns(
    dataframe: pl.DataFrame, column_mappings: Dict[str, Dict[str, str]]
) -> pl.DataFrame:
    """

    :param dataframe: A Footy Dataset to manipulate.
    :param column_mappings:
    :return:
    """
    current_columns = dataframe.columns
    columns_that_dont_exist = [
        col["mapped_column_name"]
        for col in column_mappings.values()
        if col["mapped_column_name"] not in current_columns
    ]

    return dataframe.with_columns(
        lit(None).alias(str(col)) for col in columns_that_dont_exist
    )


def get_unique_team_names(
    dataframe: pl.DataFrame, home_team_col: str, away_team_col: str
) -> List[str]:
    """Convert unique team names to a list.

    :param dataframe: a polars dataframe with footy data
    :param home_team_col: home team column name
    :param away_team_col: away team column name
    :return: List of unique team names.
    """
    unique_teams = (
        dataframe.select([home_team_col, away_team_col])
        .melt()
        .select(col("value").unique())
    )
    return [name for name in unique_teams.to_series().to_list() if name]
