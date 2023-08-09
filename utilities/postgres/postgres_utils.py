from typing import List

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import psycopg2
import os
from utilities.dataframe_util import DataframeUtil, ColumnUtils
from utilities.logger import Logger


class PostgresUtils:

    def __init__(self, table_name: str = None):
        self.dotEnv = load_dotenv()
        self.db_name = os.getenv("POSTGRES_DB")
        self.host = os.getenv("POSTGRES_HOST")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.port = os.getenv("POSTGRES_PORT")
        self.logger = Logger(logger_name="PostgresUtils")
        self.column_util = ColumnUtils()
        if table_name:
            self.table_name = table_name
        else:
            self.table_name = os.getenv("TABLE_NAME")

    def connection(self):
        try:
            return psycopg2.connect(
                host=self.host,
                database=self.db_name,
                user=self.user,
                password=self.password,
                port=self.port
            )
        except psycopg2.Error as e:
            self.logger.error(f"An error has occurred connecting to postgres: {e}")

    def create_engine(self):
        return create_engine(f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}")

    def execute(self, query: str) -> None:
        connection = self.connection()
        cursor = connection.cursor()

        try:
            self.logger.info(f"executing query: {query}")
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            self.logger.error(f"An error has occurred executing the query provided: {e}")

    def grab_data(self, query: str):
        connection = self.connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query)

            return cursor.fetchall()
        except Exception as e:
            self.logger.error(f"An error has occurred: {e}")

    # TODO: Move this to other Class, this should just be a create table method or something
    def create_table_from_existing_dataframe(self, dataframe) -> None:
        df = self.column_util.remove_col_name_string_starts_with(dataframe, "unnamed")
        columns = self.add_quotes(df.columns)
        data_types = DataframeUtil().grab_dtypes(df)

        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                {' ,'.join(' '.join(x) for x in zip(columns, data_types))}
            )
        """
        self.execute(query)

    def upload_dataframe(self, dataframe: pd.DataFrame, msg: str = None) -> None:
        try:
            self.logger.info(f"Writing Dataframe to postgres table {self.db_name}.{self.table_name}: {msg}")
            dataframe.to_sql(name=self.table_name, con=self.create_engine(), if_exists="append", index=False)
            self.connection().commit()
            self.connection().close()
        except Exception as e:
            self.logger.error(f"An error has occurred: {e}")

    def grab_table_schema(self) -> List[str]:
        query = f"""
            select column_name from information_schema.columns 
            where table_name='{self.table_name}';
        """

        return [row[0] for row in self.grab_data(query)]

    def get_high_water_mark_time(self, league_name: str) -> str:
        # Use this to get the high water-mark column for a given league
        query = f"""
            select max(date) from {self.table_name} where division = '{league_name}'
        """

        return str(self.grab_data(query)[0][0])

    def create_distinct_teams_table(self) -> None:
        query: str = f"""
            CREATE TABLE IF NOT EXISTS teams AS SELECT DISTINCT(home_team) as team_name, home_id as team_id 
            from {self.table_name}
        """

        self.execute(query)

    def get_existing_team_ids(self, list_of_teams: List[str]) -> List[str]:
        query = f"""
            SELECT team_name, team_id FROM teams 
            WHERE team_name IN ({','.join(self.add_quotes(list_of_teams, True))})
        """

        _ids = self.grab_data(query)

        return _ids

    @staticmethod
    def add_quotes(lst: List[str], single_quote: bool = None) -> List[str]:
        if single_quote:
            return [f"'{item}'" for item in lst]
        else:
            return [f'"{item}"' for item in lst]
