import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
from utilities.dataframe_util import DataframeUtil


class TestDataframeUtils(unittest.TestCase):

    def setUp(self) -> None:
        self.dataframe_utils = DataframeUtil()
        self.test_path = "https://www.football-data.co.uk/mmz4281/2223/E0.csv"
        self.test_ids = [1, 2, 3]
        self.test_names = ["premier_leage", "serie_a", "la_liga"]
        self.test_names_none = [None, None, None]
        self.test_times = ["2023-05-29", "2023-05-31", "2000-01-01"]
        self.test_times_none = [None, None, None]
        self.test_dataframe = pd.DataFrame(zip(self.test_ids, self.test_names, self.test_times),
                                           columns=["id", "div", "date"])
        self.test_dataframe_missing_cols = pd.DataFrame(self.test_ids, columns=["id"])
        self.cleaned_dataframe = pd.DataFrame(zip(self.test_ids, self.test_names_none, self.test_times_none),
                                              columns=["id", "date", "div"])
        self.uppercase_dataframe = pd.DataFrame(zip(self.test_ids, self.test_names_none, self.test_times_none),
                                                columns=["id", "date", "div"])
        self.unnamed_dataframe = pd.DataFrame(zip(self.test_ids, self.test_names_none, self.test_times_none,
                                                  self.test_times_none, self.test_times_none),
                                              columns=["id", "date", "div", "Unnamed", "unnamed"])
        self.empty_dataframe = pd.DataFrame(zip(self.test_ids, self.test_names_none, self.test_times_none),
                                            columns=["id", "date", "div"])
        self.paths = ["https://www.football-data.co.uk/mmz4281/2223/E0.csv",
                      "https://www.football-data.co.uk/mmz4281/1819/E1.csv"]

    def test_get_dataframe(self):
        dataframe = self.dataframe_utils.get_dataframe(self.test_path)
        self.assertIsNotNone(dataframe)

    def test_find_all_columns(self):
        cols = self.dataframe_utils.find_all_column_names([self.test_dataframe])
        self.assertEqual(cols, {"id", "date", "div"})

    def test_add_missing_columns_to_dataframe(self):
        cols = self.dataframe_utils.find_all_column_names([self.test_dataframe])
        cleaned_dataframe = self.dataframe_utils. \
            add_missing_columns_to_dataframe(cols, [self.test_dataframe_missing_cols])

        assert_frame_equal(cleaned_dataframe[0], self.cleaned_dataframe)

    def test_create_dataframe_list(self):
        dataframes = self.dataframe_utils.create_dataframe_list(self.paths)

        assert (len(dataframes) == 2)
        self.assertIsNotNone(dataframes[0])
        self.assertIsNotNone(dataframes[1])

    def test_get_lowercase_columns(self):
        self.uppercase_dataframe.columns = map(str.lower, self.uppercase_dataframe.columns)
        self.assertEqual(list(self.uppercase_dataframe.columns), ["id", "date", "div"])

    def test_remove_col_name_string_starts_with(self):
        dataframe = self.dataframe_utils.remove_col_name_string_starts_with(self.unnamed_dataframe, "unnamed")
        assert_frame_equal(dataframe, self.empty_dataframe)

    def test_replace_values_in_dataframe(self):
        bad_vals = ["#", "#", "@"]
        dataframe = pd.DataFrame(zip(self.test_ids, bad_vals), columns=["id", "bad_vals"])
        cleaned_dataframe = self.dataframe_utils.replace_values_in_dataframe(dataframe, "#")
        cleaned_dataframe = self.dataframe_utils.replace_values_in_dataframe(cleaned_dataframe, "@")

        assert_frame_equal(cleaned_dataframe, pd.DataFrame(zip(self.test_ids, self.test_names_none),
                                                           columns=["id", "bad_vals"]))

    def tearDown(self) -> None:
        pass

