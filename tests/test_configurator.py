"""Tests for the configurator module."""

import unittest

from configuration.configuration_enums import Country, Leagues, Source, SourceType
from configuration.configurator import Configurator


class TestConfigurator(unittest.TestCase):
    """Test cases for the Configurator class."""

    def setUp(self) -> None:
        """Set up the test cases."""
        self.test_conf: dict = {
            Country.ENGLAND: {
                "country": Country.ENGLAND,
                "leagues": [Leagues.PREMIER_LEAGUE, Leagues.CHAMPIONSHIP],
                "source_information": Source.FOOTBALL_DATA_UK,
            },
            Country.ITALY: {
                "country": Country.ITALY,
                "leagues": [
                    Leagues.SERIE_A,
                    Leagues.SERIE_B,
                ],
                "source_information": Source.FOOTBALL_DATA_UK,
            },
        }

        self.conf = Configurator(
            self.test_conf, Country.ENGLAND, Leagues.PREMIER_LEAGUE
        )

    def test_source_type(self):
        """Test the source type."""
        assert self.conf.source_type == SourceType.EXCEL

    def test_get_country_name(self):
        """Test getting the country name."""
        print(self.conf.country_name)

    def test_excel_identifiers(self):
        """Test getting the Excel identifiers."""
        print(self.conf.excel_identifier)
