import testing.postgresql
import unittest
from postgres.postgres_utils import PostgresUtils
import pandas as pd


class TestPostgresUtils(unittest.TestCase):

    def setUp(self) -> None:
        self.postgresql = testing.postgresql.Postgresql(port=7654)
        self.postgres_util = PostgresUtils()
        self.postgres_util.table_name = "testing_table"
        self.postgres_util.host = "127.0.0.1"
        self.postgres_util.db_name = "test"
        self.postgres_util.user = "postgres"
        self.postgres_util.port = "7654"
        self.postgres_util.password = 'postgres'
        self.test_table_name = "test_table"
        self.test_existing_table_name = "test_existing"
        self.test_ids = [1, 2, 3]
        self.test_names = ["premier_leage", "serie_a", "la_liga"]
        self.test_times = ["2023-05-29", "2023-05-31", "2000-01-01"]
        self.test_dataframe = pd.DataFrame(zip(self.test_ids, self.test_names, self.test_times),
                                           columns=["id", "division", "date"])

    def test_connection(self):
        assert(self.postgres_util.connection())

    def test_postgres_utils(self):
        create_table_query = f"create table if not exists {self.test_table_name} (id int, division varchar, date varchar);"
        check_schema_query = f"select * from {self.test_table_name};"
        self.postgres_util.execute(create_table_query)
        initial_data = self.postgres_util.grab_data(check_schema_query)

        self.postgres_util.upload_dataframe(self.test_dataframe)
        data = self.postgres_util.grab_data(f"select * from {self.test_table_name}")

        schema = self.postgres_util.grab_table_schema()

        max_date = self.postgres_util.get_high_water_mark_time("serie_a")

        self.postgres_util.create_table_from_existing_dataframe(self.test_dataframe)
        existing_schema = self.postgres_util.grab_table_schema()

        self.assertFalse(initial_data)
        self.assertIsNotNone(data)
        self.assertEqual(schema, ["id", "division", "date"])
        self.assertEqual(max_date, "2023-05-31")
        self.assertEqual(existing_schema, ["id", "division", "date"])

    def tearDown(self) -> None:
        self.postgresql.stop()
