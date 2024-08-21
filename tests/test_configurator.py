import unittest

from configuration.configuration_enums import Country, Leagues, Source, SourceType
from configuration.configurator import Configurator


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
            },
            Country.ITALY: {
                "country": Country.ITALY,
                "leagues": [
                    Leagues.SERIE_A,
                    Leagues.SERIE_B,
                ],
                "source_information": Source.FOOTBALL_DATA_UK
            }
        }

        self.conf = Configurator(self.test_conf, Country.ENGLAND, Leagues.PREMIER_LEAGUE)

    def test_source_type(self):
        assert self.conf.source_type == SourceType.EXCEL

    def test_get_country_name(self):
        print(self.conf.country_name)

    def test_excel_identifiers(self):
        print(self.conf.excel_identifier)

    def test_country_link(self):
        print(self.conf.country_link)
