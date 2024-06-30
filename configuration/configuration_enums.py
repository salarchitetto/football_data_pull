"""

"""

from enum import Enum
from typing import Union
from dataclasses import dataclass


class SourceType(Enum):
    EXCEL = 0
    API = 1
    SCRAPER = 2

    @classmethod
    def from_name(cls, source_type: str) -> "SourceType":
        return cls[source_type.lower()]


@dataclass
class SourceData:
    alternative_name: str
    website_link: str
    source_type: SourceType
    excel_file_name: Union[str, None]  # Mainly for the UK website data


@dataclass
class LeagueData:
    excel_identifier_name: Union[str, None]


class Source(Enum):
    """
    A list of source that are available to pull from in this program.
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
        try:
            return cls[source_name.lower()]
        except KeyError as ke:
            raise ValueError(f"Please choose an available source: {ke}")


class Country(Enum):
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
    """
    Every league available to the platform currently. For right now this
    is mainly geared towards Europe but will expand as more data comes in.
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
        return cls[league_name.lower()]
