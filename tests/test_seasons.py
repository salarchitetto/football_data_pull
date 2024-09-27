"""Test cases for the Seasons Module."""

import unittest

from configuration.configuration_enums import Country, Leagues
from configuration.configurator import Configurator
from configuration.football_data_uk_configuration import football_data_uk
from utilities.season_formatter import SeasonDates


class TestSeasons(unittest.TestCase):
    """Test Seasons Module."""

    def setUp(self) -> None:
        """Set up the test cases."""
        self.conf_without_limit = Configurator(
            football_data_uk, Country.ENGLAND, Leagues.PREMIER_LEAGUE
        )
        self.season_dates_without_limit = SeasonDates(self.conf_without_limit)
        self.conf_with_limit = Configurator(
            football_data_uk, Country.BELGIUM, Leagues.BELGIUM_PRO_LEAGUE
        )
        self.season_dates_with_limit = SeasonDates(self.conf_with_limit, 100)

    def test_multiple_paths(self):
        """Test multiple paths."""
        print(self.season_dates_without_limit.get_csv_download_paths())

    def test_limit_multiple_paths(self):
        """Test limiting multiple paths."""
        print(self.season_dates_with_limit.get_csv_download_paths())

    def test_formatted_seasons_list(self):
        """Test formatted seasons list."""
        print(self.season_dates_with_limit.get_formatted_seasons_list())
