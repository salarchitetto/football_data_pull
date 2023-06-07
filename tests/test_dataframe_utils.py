import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal
from tests.testing_dataframes import TestingDataframes
from utilities.dataframe_util import DataframeUtil


class TestDataframeUtils(unittest.TestCase):

    def setUp(self) -> None:
        self.dataframe_utils = DataframeUtil()
        self.testing_dataframes = TestingDataframes()
        self.test_path = "https://www.football-data.co.uk/mmz4281/2223/E0.csv"
        self.paths = ["https://www.football-data.co.uk/mmz4281/2223/E0.csv",
                      "https://www.football-data.co.uk/mmz4281/1819/E1.csv"]

    def test_get_dataframe(self):
        dataframe = self.dataframe_utils.get_dataframe(self.test_path)
        self.assertIsNotNone(dataframe)

    def test_create_dataframe_list(self):
        dataframes = self.dataframe_utils.create_dataframe_list(self.paths)

        assert (len(dataframes) == 2)
        self.assertIsNotNone(dataframes[0])
        self.assertIsNotNone(dataframes[1])

    def test_replace_values_in_dataframe(self):
        bad_vals = ["#", "#", "@"]
        dataframe = pd.DataFrame(zip(self.testing_dataframes.test_ids, bad_vals), columns=["id", "bad_vals"])
        cleaned_dataframe = self.dataframe_utils.replace_values_in_dataframe(dataframe, "#")
        cleaned_dataframe = self.dataframe_utils.replace_values_in_dataframe(cleaned_dataframe, "@")

        assert_frame_equal(cleaned_dataframe, pd.DataFrame(zip(self.testing_dataframes.test_ids,
                                                               self.testing_dataframes.test_names_none),
                                                           columns=["id", "bad_vals"]))

    def tearDown(self) -> None:
        pass

