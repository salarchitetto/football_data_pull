from typing import Optional

from configuration.configuration_enums import Country, SourceType, Leagues


class Configurator:
    """
    The Configurator class handles the configuration data for a specific country and league.
    It provides access to various attributes such as league names, Excel identifiers, and source information.

    Attributes:
        country (Country): The country for which the configuration is being accessed.
        league (Leagues): The league within the specified country.
        conf (dict): The configuration data for the specified country.
    """

    def __init__(self, conf: dict, country: Country, league: Leagues):
        """
        Initializes the Configurator instance with the given configuration, country, and league.

        :param conf: A dictionary containing configuration data for various countries.
        :param country: The country for which the configuration is being accessed.
        :param league: The league within the specified country.
        :raises ValueError: If the configuration for the country or league is not found.
        """
        self.country = country
        self.league = league
        self.conf = conf.get(self.country)

        if not self.conf:
            raise ValueError(f"Configuration for country {self.country.name} not found.")

        if self.league not in self.conf.get("leagues", []):
            raise ValueError(f"League '{self.league.name}' is not part of the configuration for country {self.country}.")

    def _find_league(self):
        """
        Finds and returns the league data for the specified league within the country's configuration.

        :return: The league data for the specified league.
        :raises ValueError: If the league is not found in the configuration.
        """
        leagues = self.conf.get("leagues", [])
        for league in leagues:
            if league == self.league:
                return league
        raise ValueError(f"League '{self.league.name}' not found in configuration.")

    @property
    def country_name(self) -> str:
        """
        Returns the name of the country in lowercase.

        :return: The lowercase name of the country.
        """
        return self.conf["country"].name.lower()

    @property
    def league_name(self) -> str:
        """
        Returns the name of the league in lowercase.

        :return: The lowercase name of the league.
        """
        return self._find_league().name.lower()

    @property
    def excel_identifier(self) -> str:
        """
        Returns the Excel identifier for the specified league.

        :return: The uppercase Excel identifier for the league.
        :raises ValueError: If the league is not found in the configuration.
        """
        return self._find_league().value.excel_identifier_name.upper()

    @property
    def alternative_source_name(self) -> str:
        """
        Returns the alternative source name for the data source.

        :return: The lowercase alternative source name.
        :raises ValueError: If source information is not found in the configuration.
        """
        source_info = self.conf.get("source_information")
        if not source_info:
            raise ValueError(f"Source information not found in configuration for {self.country_name}.")
        return source_info.value.alternative_name.lower()

    @property
    def website_link(self) -> str:
        """
        Returns the website link for the data source.

        :return: The lowercase website link.
        """
        return self.conf["source_information"].value.website_link.lower()

    @property
    def source_type(self) -> SourceType:
        """
        Returns the source type for the data source.

        :return: The source type.
        """
        return self.conf["source_information"].value.source_type

    @property
    def excel_link(self) -> str:
        """
        Returns the Excel download link for the data source.

        :return: The lowercase Excel download link.
        """
        return self.conf["source_information"].value.excel_link.lower()

    @property
    def excel_file_name(self) -> Optional[str]:
        """
        Returns the Excel file name for the data source, if available.

        :return: The Excel file name or None if not available.
        """
        return self.conf["source_information"].value.excel_file_name
