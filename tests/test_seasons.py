import unittest

from configuration.configuration_enums import Country, Leagues, Source, SourceType
from configuration.configurator import Configurator
from football_data_uk.season_dates import SeasonDates


class TestConfigurator(unittest.TestCase):

    def setUp(self) -> None:
        self.test_conf: dict = {
            Country.ENGLAND: {
                "country": Country.ENGLAND,
                "leagues": [
                    Leagues.PREMIER_LEAGUE,
                    Leagues.CHAMPIONSHIP
                ],
                "source_information": Source.FOOTBALL_DATA_UK
            }
        }

        self.conf_without_limit = Configurator(self.test_conf, Country.ENGLAND, Leagues.PREMIER_LEAGUE)
        self.season_dates_without_limit = SeasonDates(self.conf_without_limit)
        self.conf_with_limit = Configurator(self.test_conf, Country.ENGLAND, Leagues.PREMIER_LEAGUE)
        self.season_dates_with_limit = SeasonDates(self.conf_with_limit, 5)

    def test_get_current_season_link(self):
        print(self.season_dates_without_limit.get_current_season_download_path())

    def test_multiple_paths(self):
        print(self.season_dates_without_limit.get_multiple_season_download_paths())

    def test_limit_multiple_paths(self):
        print(self.season_dates_with_limit.get_multiple_season_download_paths())
