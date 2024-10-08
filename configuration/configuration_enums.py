"""A bunch of configuration methods and classes for the application.

Will write more as I go.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class SourceType(Enum):
    """The source type for the incoming data."""

    EXCEL = 0
    API = 1
    SCRAPER = 2

    @classmethod
    def from_name(cls, source_type: str) -> "SourceType":
        """Return a lowered string version of the above enums.

        :param source_type: source type name.
        :return: return the name of the source type.
        """
        return cls[source_type.lower()]


@dataclass
class SourceData:
    """Some base information for the source data."""

    alternative_name: str
    website_link: str
    source_type: SourceType
    excel_file_name: Optional[str]  # Mainly for the UK website data

    def __post_init__(self) -> None:
        """Values adhere to the types instantiated above.

        :return: None
        """
        if not isinstance(self.alternative_name, str):
            raise TypeError(f"Expected String, got {type(self.alternative_name)}")

        if not isinstance(self.website_link, str):
            raise TypeError(f"Expected String, got {type(self.website_link)}")

        if not isinstance(self.source_type, SourceType):
            raise TypeError(f"Expected SourceType, got {type(self.source_type)}")

        if not (self.excel_file_name is None or isinstance(self.excel_file_name, str)):
            raise TypeError(
                f"Expected String or None, got {type(self.excel_file_name)}"
            )

    @property
    def excel_link(self) -> str:
        """Return an Excel link (Used for football_data_uk).

        :return: Path to the starter of an Excel link.
        The rest is created via the SeasonFormatter
        """
        return f"{self.website_link}/{self.excel_file_name}"


@dataclass
class LeagueData:
    """Data class for league data."""

    excel_identifier_name: str

    def __post_init__(self) -> None:
        """Type checking for the league data.

        :return:
        """
        if not isinstance(self.excel_identifier_name, str):
            raise TypeError(f"Expected String, got {type(self.excel_identifier_name)}")


class Source(Enum):
    """A list of source that are available to pull from in this program.

    These are set up with the SourceData dataclass that houses general
    information from the source.
    To access this information you can do something like:
    Source.FOOTBALL_DATA_UK.value.alternative_name
    """

    FOOTBALL_DATA_UK = SourceData(
        alternative_name="football_data_uk",
        website_link="https://www.football-data.co.uk",
        source_type=SourceType.EXCEL,
        excel_file_name="mmz4281",
    )

    @classmethod
    def from_name(cls, source_name: str) -> "Source":
        """Return a lowered string version of the above enums.

        :param source_name: source type name.
        :return: return the name of the source type.
        """
        try:
            return cls[source_name.lower()]
        except KeyError as ke:
            raise ValueError(f"Please choose an available source: {ke}")


class Country(Enum):
    """Country Enums that are provided in this application."""

    BELGIUM = 0
    ENGLAND = 1
    FRANCE = 2
    GERMANY = 3
    ITALY = 4
    NETHERLANDS = 5
    PORTUGAL = 6
    SCOTLAND = 7
    SPAIN = 8


class Leagues(Enum):
    """Every league available to the platform currently.

    For right now this is mainly geared towards Europe
    but will expand as more data comes in.

    This Enum Class will take in a dataclass payload called LeagueData,
    which will hopefully make sense and house information about the league/
    configurations around it.
    """

    BELGIUM_PRO_LEAGUE = LeagueData(excel_identifier_name="B1")
    BUNDESLIGA = LeagueData(excel_identifier_name="D1")
    BUNDESLIGA_2 = LeagueData(excel_identifier_name="D2")
    CHAMPIONSHIP = LeagueData(excel_identifier_name="E1")
    EREDIVISIE = LeagueData(excel_identifier_name="N1")
    LA_LIGA = LeagueData(excel_identifier_name="SP1")
    LA_LIGA_2 = LeagueData(excel_identifier_name="SP2")
    LIGA_PORTUGAL = LeagueData(excel_identifier_name="P1")
    LIGUE_1 = LeagueData(excel_identifier_name="F1")
    LIGUE_2 = LeagueData(excel_identifier_name="F2")
    PREMIER_LEAGUE = LeagueData(excel_identifier_name="E0")
    SCOTTISH_CHAMPIONSHIP = LeagueData(excel_identifier_name="SC0")
    SCOTTISH_PREMIERSHIP = LeagueData(excel_identifier_name="SC1")
    SERIE_A = LeagueData(excel_identifier_name="I1")
    SERIE_B = LeagueData(excel_identifier_name="I2")

    @classmethod
    def from_name(cls, league_name: str) -> "Leagues":
        """Return a lowered string version of the above enums.

        :param league_name: source type name.
        :return: return the name of the source type.
        """
        return cls[league_name.lower()]
