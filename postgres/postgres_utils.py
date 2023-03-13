from typing import List
from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import os

from utilities.dataframe_util import DataframeUtil
from utilities.directories import Directories


class PostgresUtils:
    """
    TODO: squash all the dataframes into one
    use directories class to grab all dataframes
    use DataframeUtils to union all of the together
    create helper class to automate CREATE TABLE sql query from unified dataframe
    insert into new table - insert()
    create_table()

    """

    def __init__(self,
                 _all: bool = True,
                 league: str = None):
        self._all = all
        self.league = league
        self.db_name = "footy"
        self.host = "localhost"
        self.user = os.environ["DB_USER"]
        self.password = os.environ["DB_PASSWORD"]
        self.outcomes_table = "results"

    def connection(self):
        try:
            return psycopg2.connect(
                host=self.host,
                database=self.db_name,
                user=self.user,
                password=self.password
            )
        except psycopg2.Error as e:
            print(f"An error has occurred connecting to postgres: {e}")

    def create_engine(self):
        return create_engine(f"postgresql://{self.user}:{self.password}@localhost:5432/{self.db_name}")

    def execute(self, query: str) -> None:
        connection = self.connection()
        cursor = connection.cursor()

        try:
            print(f"executing query: {query}")
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(f"An error has occurred executing the query provided: {e}")

    def grab_data(self, query: str):
        connection = self.connection()
        cursor = connection.cursor()

        try:
            cursor.execute(query)

            return cursor.fetchall()
        except Exception as e:
            print(f"An error has occurred: {e}")

    def create_team_outcomes_table(self, dataframe) -> None:
        df = self.extra_clean(dataframe)
        columns = self.add_quotes(df.columns)
        data_types = self.grab_dtypes(df)

        query = f"""
            CREATE TABLE IF NOT EXISTS {self.outcomes_table} (
                {' ,'.join(' '.join(x) for x in zip(columns, data_types))}
            )
        """
        print(query)
        self.execute(query)

    def upload_dataframe(self, dataframe) -> None:
        try:
            print(f"Writing Dataframe to postgres table {self.db_name}.{self.outcomes_table}")
            dataframe.to_sql(name=self.outcomes_table, con=self.create_engine(), if_exists="append", index=False)
            self.connection().commit()
            self.connection().close()
        except Exception as e:
            print(f"An error has occurred: {e}")

    def grab_results_schema(self) -> List[str]:
        query = f"""
            select column_name from information_schema.columns 
            where table_name='{self.outcomes_table}';
        """
        print(query)
        return [row[0] for row in self.grab_data(query)]

    def grab_dtypes(self, dataframe: pd.DataFrame) -> List[str]:

        dtypes = []
        for keys, values in dataframe.dtypes.items():
            dtypes.append(values.name)

        return self.type_checker(dtypes)

    @staticmethod
    def type_checker(dtype_list: List[str]) -> List[str]:
        return list(map(lambda x: x.
                        replace("object", "text")
                        .replace("float64", "float")
                        .replace("int64", "integer"),
                        dtype_list))

    @staticmethod
    def add_quotes(lst: List[str]) -> List[str]:
        return [f'"{item}"' for item in lst]

    @staticmethod
    def extra_clean(dataframe: pd.DataFrame) -> pd.DataFrame:
        return dataframe.loc[:, ~dataframe.columns.str.startswith("Unnamed")]
