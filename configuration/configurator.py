""""""
from typing import Optional

from configuration.configuration_enums import Country, SourceType, Leagues
from configuration.football_data_uk_configuration import football_data_uk


class Configurator(object):

    def __init__(self, conf: dict, country: Country, league: Leagues):
        self.country = country
        self.league = league
        self.conf = conf.get(self.country)

        if not self.conf:
            raise ValueError(f"Configuration for country {self.country.name} not found.")

        if self.league not in self.conf.get("leagues", []):
            raise ValueError(f"League '{self.league.name}' is not part of the configuration for country {self.country}.")

    def _find_league(self):
        leagues = self.conf.get("leagues", [])
        for league in leagues:
            if league == self.league:
                return league
        raise ValueError(f"League '{self.league.name}' not found in configuration.")

    @property
    def country_name(self) -> str:
        return self.conf["country"].name.lower()

    @property
    def league_name(self) -> str:
        return self._find_league().name.lower()

    @property
    def excel_identifier(self) -> str:
        """
        Returns the Excel identifier for the specified league.
        """
        return self._find_league().value.excel_identifier_name.upper()

    @property
    def alternative_source_name(self) -> str:
        source_info = self.conf.get("source_information")
        if not source_info:
            raise ValueError(f"Source information not found in configuration for {self.country_name}.")
        return source_info.value.alternative_name.lower()

    @property
    def website_link(self) -> str:
        return self.conf["source_information"].value.website_link.lower()

    @property
    def source_type(self) -> SourceType:
        return self.conf["source_information"].value.source_type

    @property
    def excel_link(self) -> str:
        return self.conf["source_information"].value.excel_link.lower()

    @property
    def excel_file_name(self) -> Optional[str]:
        return self.conf["source_information"].value.excel_file_name


configurator = Configurator(football_data_uk, Country.SPAIN, Leagues.LA_LIGA)
