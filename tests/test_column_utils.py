import unittest
from pandas.util.testing import assert_frame_equal
from utilities.dataframe_util import ColumnUtils
from tests.testing_dataframes import TestingDataframes


class TestColumnUtils(unittest.TestCase):
    def setUp(self) -> None:
        self.column_utils = ColumnUtils()
        self.testing_dataframes = TestingDataframes()

    def test_find_all_columns(self):
        cols = self.column_utils.find_all_column_names([self.testing_dataframes.test_dataframe])
        self.assertEqual(cols, {"id", "date", "division"})

    def test_add_missing_columns_to_dataframe(self):
        cols = self.column_utils.find_all_column_names([self.testing_dataframes.test_dataframe])
        cleaned_dataframe = self.column_utils. \
            add_missing_columns_to_dataframe(cols, [self.testing_dataframes.test_dataframe_missing_cols])

        assert_frame_equal(
            cleaned_dataframe[0].reindex(sorted(cleaned_dataframe[0].columns), axis=1),
            self.testing_dataframes.cleaned_dataframe.reindex(sorted(self.testing_dataframes.cleaned_dataframe.columns),
                                                              axis=1))

    def test_get_lowercase_columns(self):
        self.testing_dataframes.uppercase_dataframe.columns = map(
            str.lower, self.testing_dataframes.uppercase_dataframe.columns)
        self.assertEqual(list(self.testing_dataframes.uppercase_dataframe.columns), ["id", "date", "division"])

    def test_remove_col_name_string_starts_with(self):
        dataframe = self.column_utils.remove_col_name_string_starts_with(
            self.testing_dataframes.unnamed_dataframe, "unnamed")
        assert_frame_equal(dataframe, self.testing_dataframes.empty_dataframe)

    def tearDown(self) -> None:
        pass



