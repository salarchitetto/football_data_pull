import unittest


from configuration.configuration_enums import Country, Leagues
from configuration.configurator import Configurator
from configuration.football_data_uk_configuration import football_data_uk, FOOTBALL_DATA_UK_MAPPING
from utilities.footy_dataframes import read_csv, add_new_static_column, convert_column_name, \
    convert_unformatted_dates, clean_team_names, convert_multiple_column_names, select_columns_that_exist
from utilities.season_formatter import SeasonDates


class TestConfigurator(unittest.TestCase):

    def setUp(self) -> None:
        self.conf_without_limit = Configurator(football_data_uk, Country.ENGLAND, Leagues.PREMIER_LEAGUE)
        self.season_dates_without_limit = SeasonDates(self.conf_without_limit)
        self.conf_with_limit = Configurator(football_data_uk, Country.BELGIUM, Leagues.BELGIUM_PRO_LEAGUE)
        self.season_dates_with_limit = SeasonDates(self.conf_with_limit, 100)

    def test_multiple_paths(self):
        print(self.season_dates_without_limit.get_csv_download_paths())

    def test_limit_multiple_paths(self):
        print(self.season_dates_with_limit.get_csv_download_paths())

    def test_formatted_seasons_list(self):
        print(self.season_dates_with_limit.get_formatted_seasons_list())

    def test_polars_read(self):
        csv_path = self.season_dates_without_limit.get_csv_download_paths()[0]
        print(csv_path)
        dataframe = (
            read_csv(csv_path)
            .pipe(add_new_static_column, "test", "this_works")
            .pipe(convert_column_name, "testing", "test")
            # .pipe(convert_unformatted_dates, "Date", "%y-%m-%d")
            # # .pipe(clean_team_names, ["HomeTeam", "AwayTeam"])
            # # .pipe(convert_multiple_column_names, {"HomeTeam": "home_team", "AwayTeam": "away_team", "Date": "date"})
            .pipe(convert_multiple_column_names, FOOTBALL_DATA_UK_MAPPING)
            .pipe(select_columns_that_exist, FOOTBALL_DATA_UK_MAPPING)
        )
        import polars as pl
        pl.Config.set_tbl_rows(2000)
        # print(dataframe.select("date", "home_team", "away_team").unique().sort(by="date"))
        print(dataframe)