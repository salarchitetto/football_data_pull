import unittest
from utilities.configurator import Configurator
from utilities.season_formatter import SeasonDates


class TestSeasonDates(unittest.TestCase):
    def setUp(self) -> None:
        self.configs = Configurator()
        self.season_dates = SeasonDates(self.configs)
        self.season_list = ["2324","2223", "2122", "2021", "1920",
                            "1819", "1718", "1617", "1516",
                            "1415", "1314", "1213", "1112",
                            "1011", "910", "89", "78", "67",
                            "56", "45", "34", "23", "12", "01"]
        self.season_check_list = ["2223", "1819", "910", "56", "01"]
        self.season_path_list_check = ["2223", "1819", "0910", "0506", "0001"]
        self.path_check_list = ["https://www.football-data.co.uk/mmz4281/2223/None.csv",
                                "https://www.football-data.co.uk/mmz4281/1819/None.csv",
                                "https://www.football-data.co.uk/mmz4281/0910/None.csv",
                                "https://www.football-data.co.uk/mmz4281/0506/None.csv",
                                "https://www.football-data.co.uk/mmz4281/0001/None.csv"]

    def test_get_years_list(self):
        self.assertEqual(self.season_dates.get_years_list(), self.season_list)

    def test_get_this_season(self):
        self.assertEqual(self.season_dates.get_years_list()[0], self.season_list[0])

    def test_get_seasons_list(self):
        years = self.season_dates.get_seasons_list(self.season_check_list)
        case_4 = ["2223", "1819"]
        case_3 = "0910"
        case_2 = "0506"
        case_ = "0001"

        self.assertEqual(case_4, years[0:2])
        self.assertEqual(case_3, years[2])
        self.assertEqual(case_2, years[3])
        self.assertEqual(case_, years[4])

    def test_get_current_season_download_paths(self):
        path = self.season_dates.get_current_season_download_path()
        self.assertEqual(path, "https://www.football-data.co.uk/mmz4281/2324/None.csv")

    def test_multiple_season_download_paths(self):
        seasons = self.season_dates.get_multiple_season_download_paths(self.season_path_list_check)
        self.assertEqual(seasons, self.path_check_list)

    def tearDown(self) -> None:
        pass
