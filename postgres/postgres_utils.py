from typing import List
from sqlalchemy import create_engine
from dotenv import load_dotenv
import psycopg2
import os
from utilities.dataframe_util import DataframeUtil
from utilities.logger import Logger


class PostgresUtils:

    def __init__(self, _all: bool = True, league: str = None):
        self._all = all
        self.league = league
        self.db_name = "footy"
        self.host = "localhost"
        self.dotEnv = load_dotenv()
        self.user = os.getenv("POSTGRES_USERNAME")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.logger = Logger(logger_name="PostgresUtils")

    def connection(self):
        try:
            return psycopg2.connect(
                host=self.host,
                database=self.db_name,
                user=self.user,
                password=self.password
            )
        except psycopg2.Error as e:
            self.logger.error(f"An error has occurred connecting to postgres: {e}")

    def create_engine(self):
        return create_engine(f"postgresql://{self.user}:{self.password}@localhost:5432/{self.db_name}")

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
    def create_table_from_existing_dataframe(self, dataframe, table_name: str) -> None:
        df = DataframeUtil().remove_unnamed_from_column_name(dataframe)
        columns = self.add_quotes(df.columns)
        data_types = DataframeUtil().grab_dtypes(df)

        query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {' ,'.join(' '.join(x) for x in zip(columns, data_types))}
            )
        """
        self.execute(query)

    def upload_dataframe(self, dataframe, table_name: str) -> None:
        try:
            self.logger.info(f"Writing Dataframe to postgres table {self.db_name}.{table_name}")
            dataframe.to_sql(name=table_name, con=self.create_engine(), if_exists="append", index=False)
            self.connection().commit()
            self.connection().close()
        except Exception as e:
            self.logger.error(f"An error has occurred: {e}")

    def grab_results_schema(self, table_name: str) -> List[str]:
        query = f"""
            select column_name from information_schema.columns 
            where table_name='{table_name}';
        """

        return [row[0] for row in self.grab_data(query)]

    def get_high_water_mark_time(self, league_name: str, table_name: str) -> str:
        # Use this to get the high water-mark column for a given league
        query = f"""
            select max(date) from {table_name} where div = '{league_name}'
        """

        return str(self.grab_data(query)[0][0])

    @staticmethod
    def add_quotes(lst: List[str]) -> List[str]:
        return [f'"{item}"' for item in lst]
