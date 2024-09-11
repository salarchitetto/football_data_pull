import traceback
from typing import Optional, Any

import polars as pl
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import psycopg2
import os
from utilities.logger import Logger


class FootyPostgres:
    """
    A utility class for managing PostgreSQL connections, executing queries,
    and interacting with Polars DataFrames.
    """

    def __init__(self, query: Optional[str] = None, table_name: Optional[str] = None):
        load_dotenv()
        self.query = query
        self.table_name = table_name
        self.db_name = os.getenv("POSTGRES_DB")
        self.host = os.getenv("POSTGRES_HOST")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.port = os.getenv("POSTGRES_PORT")
        self.uri = f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"
        self.logger = Logger(logger_name="FootyPostgres")

    def _connect(self):
        """
        Establishes and returns a PostgreSQL database connection.

        :return: A psycopg2 connection object.
        """
        try:
            return psycopg2.connect(
                host=self.host,
                database=self.db_name,
                user=self.user,
                password=self.password,
                port=self.port,
                cursor_factory=RealDictCursor
            )
        except psycopg2.Error as e:
            self.logger.error(f"Failed to connect to PostgreSQL: {e}")
            self.logger.error(traceback.format_exc())
            raise

    def __enter__(self):
        """
        Enters the runtime context for the connection, returning the connection and cursor.

        :return: A tuple of the connection and cursor objects.
        """
        self.conn = self._connect()
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes the cursor and connection when exiting the runtime context.

        :param exc_type: The type of the exception.
        :param exc_val: The value of the exception.
        :param exc_tb: The traceback object.
        :return: None
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        if exc_type is not None:
            self.logger.error(f"Exception during database operation: {exc_type}, {exc_val}")
            self.logger.error(traceback.format_exc())

    def execute(self, query: str, params: Optional[tuple] = None, fetch_results: bool = False) -> tuple[Any, list[Any]]:
        """
        Executes a SQL query and optionally fetches the results.

        :param query: The SQL query to execute.
        :param params: A tuple of parameters to substitute in the query.
        :param fetch_results: A boolean flag indicating whether to fetch and return query results.
        :return: A list of dictionaries representing the fetched rows if fetch_results is True, otherwise None.
        """
        try:
            with self as (conn, cursor):
                cursor.execute(query, params)
                conn.commit()
                if fetch_results:
                    columns = [desc[0] for desc in cursor.description]
                    rows = cursor.fetchall()
                    return rows, columns
                self.logger.info(f"Successfully executed query. {cursor.description}")
        except Exception as e:
            self.logger.error(f"Exception during database operation: {e}")
            raise

    def fetch_dataframe(self, query: str, params: Optional[tuple] = None) -> pl.DataFrame:
        """
        Executes a SQL query and returns the results as a Polars DataFrame.

        :param query: The SQL query to execute.
        :param params: A tuple of parameters to substitute in the query.
        :return: A Polars DataFrame containing the query results.
        """
        rows, columns = self.execute(query=query, params=params, fetch_results=True)
        return pl.DataFrame(data=rows, schema={col: pl.Utf8 for col in columns})

    def _schema_creator(self, cursor_information):
        pass

    def post_dataframe(self, dataframe: pl.DataFrame, table_name: str) -> None:
        """
        Inserts the contents of a Polars DataFrame into a PostgreSQL table.

        :param dataframe: The Polars DataFrame to insert.
        :param table_name: The name of the PostgreSQL table to insert the data into.
        :return: None
        """
        dataframe.write_database(table_name=table_name, connection=self.uri, if_table_exists="append")

    def check_if_table_exists(self, table_name: str) -> bool:
        """Checks if a PostgreSQL table exists.

        :param table_name: The name of the table to check.
        :return: Boolean flag indicating if the table exists.
        """
        query = f"""
            SELECT EXISTS (
                SELECT 1
                FROM pg_tables
                WHERE tablename = '{table_name}'
            ) AS table_existence;
        """

        result = self.execute(query=query, fetch_results=True)
        self.logger.info(f"Table exists: {result}")
        return result[0]["table_existence"]