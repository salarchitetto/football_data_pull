"""Basic Utility Methods used throughout the project."""

import builtins
import datetime
from enum import Enum


def generate_create_table_query(table_name: str, mapping_dict: dict) -> str:
    """
    Generates a SQL query to create a table based on a mapping dictionary.

    :param table_name: The name of the table to create.
    :param mapping_dict: A dictionary containing prior column names
     mapped to new column names and data types.

    The dictionary should have the following structure:
        {
            "old_column_name": {
                "mapped_column_name": "new_column_name",
                "column_type": type
            }
        }
    :return: A SQL query string to create the table with the specified columns and types.
    :raises ValueError: If an unsupported column type is found in the mapping dictionary.
    """
    columns = []
    for prior_name, values in mapping_dict.items():
        new_name = values["mapped_column_name"]
        column_type = values["column_type"]

        # Match against the provided column types
        match column_type:
            case builtins.str:
                sql_type = "VARCHAR"
            case builtins.int:
                sql_type = "INTEGER"
            case builtins.float:
                sql_type = "FLOAT"
            case datetime.date | datetime.datetime:
                sql_type = "TIMESTAMP"
            case _:
                raise ValueError(f"Unsupported column type: {column_type}")

        columns.append(f"{new_name} {sql_type}")

    columns_sql = ", ".join(columns)

    # Construct the final SQL query
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        {columns_sql}
    );
    """

    return query


class TextColor(Enum):
    """Text Colors."""

    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"


def highlight_text(text, color: TextColor):
    """Highlights strings.

    :param text:
    :param color:
    :return:
    """
    return f"{color.value}{text}{TextColor.RESET.value}"
