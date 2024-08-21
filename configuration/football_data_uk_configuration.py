"""
football_data_uk configuration dictionary.
"""
from configuration.configuration_enums import Source, Country, Leagues

football_data_uk: dict = {
    Country.BELGIUM: {
        "country": Country.BELGIUM,
        "leagues": [
            Leagues.BELGIUM_PRO_LEAGUE
        ],
        "source_information": Source.FOOTBALL_DATA_UK
    },
    Country.ENGLAND: {
        "country": Country.ENGLAND,
        "leagues": [
            Leagues.PREMIER_LEAGUE,
            Leagues.CHAMPIONSHIP
        ],
        "source_information": Source.FOOTBALL_DATA_UK
    },
    Country.FRANCE: {
        "country": Country.FRANCE,
        "leagues": [
            Leagues.LIGUE_1,
            Leagues.LIGUE_2
        ],
        "source_information": Source.FOOTBALL_DATA_UK
    },
    Country.GERMANY: {
        "country": Country.GERMANY,
        "leagues": [
            Leagues.BUNDESLIGA,
            Leagues.BUNDESLIGA_2,
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
    },
    Country.NETHERLANDS: {
        "country": Country.NETHERLANDS,
        "leagues": [
            Leagues.EREDIVISIE
        ],
        "source_information": Source.FOOTBALL_DATA_UK
    },
    Country.PORTUGAL: {
        "country": Country.PORTUGAL,
        "leagues": [
            Leagues.LIGA_PORTUGAL
        ],
        "source_information": Source.FOOTBALL_DATA_UK
    },
    Country.SCOTLAND: {
        "country": Country.SCOTLAND,
        "leagues": [
            Leagues.SCOTTISH_PREMIERSHIP,
            Leagues.SCOTTISH_CHAMPIONSHIP
        ],
        "source_information": Source.FOOTBALL_DATA_UK
    },
    Country.SPAIN: {
        "country": Country.SPAIN,
        "leagues": [
            Leagues.LA_LIGA,
            Leagues.LA_LIGA_2,
        ],
        "source_information": Source.FOOTBALL_DATA_UK
    }
}
