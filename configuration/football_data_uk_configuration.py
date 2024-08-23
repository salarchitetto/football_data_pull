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

FOOTBALL_DATA_UK_MAPPING: dict = {
    "Time": "match_time",
    "Date": "date",
    "HomeTeam": "home_team",
    "AwayTeam": "away_team",
    "FTHG": "full_time_home_team_goals",
    "FTAG": "full_time_away_team_goals",
    "FTR": "full_time_result",
    "HTHG": "half_time_home_team_goals",
    "HTAG": "half_time_away_team_goals",
    "HTR": "half_time_result",
    "HS": "home_team_shots",
    "AS": "away_team_shots",
    "HST": "home_team_shots_on_target",
    "AST": "away_team_shots_on_target",
    "HF": "home_team_fouls",
    "AF": "away_team_fouls",
    "HC": "home_team_corners",
    "AC": "away_team_corners",
    "HY": "home_team_yellow_cards",
    "AY": "away_team_yellow_cards",
    "HR": "home_team_red_cards",
    "AR": "away_team_red_cards",
    "HFKC": "home_team_free_kicks",
    "AFKC": "away_team_free_kicks",
    "B365H": "bet_365_home_odds",
    "B365D": "bet_365_draw_odds",
    "B365A": "bet_365_away_odds",
    "BWH": "bet_win_home_odds",
    "BWD": "bet_win_draw_odds",
    "BWA": "bet_win_away_odds",
    "IWH": "interwetten_home_odds",
    "IWD": "interwetten_draw_odds",
    "IWA": "interwetten_away_odds",
    "PSH": "pinnacle_home_odds",
    "PSD": "pinnacle_draw_odds",
    "PSA": "pinnacle_away_odds",
    "WHH": "william_hill_home_odds",
    "WHD": "william_hill_draw_odds",
    "WHA": "william_hill_away_odds",
    "VCH": "vc_bet_home_odds",
    "VCD": "vc_bet_draw_odds",
    "VCA": "vc_bet_away_odds",
    "MAXH": "market_maximum_home_odds",
    "MAXD": "market_maximum_draw_odds",
    "MAXA": "market_maximum_away_odds",
    "AVGH": "market_average_home_odds",
    "AVGD": "market_average_draw_odds",
    "AVGA": "market_average_away_odds",
    "B365>2.5": "bet_365_over_2.5_goals",
    "B365<2.5": "bet_365_under_2.5_goals",
    "P>2.5": "pinnacle_over_2.5_goals_odds",
    "P<2.5": "pinnacle_under_2.5_goals_odds",
    "MAX>2.5": "market_maximum_over_2.5_goals_odds",
    "MAX<2.5": "market_maximum_under_2.5_goals_odds",
    "AVG>2.5": "market_average_over_2.5_goals_odds",
    "AVG<2.5": "market_average_under_2.5_goals_odds",
    "AHH": "market_size_of_handicap_home_odds",
    "B365AHH": "bet_365_asian_handicap_home_odds",
    "B365AHA": "bet_365_asian_handicap_away_odds",
    "PAHH": "pinnacle_asian_handicap_home_odds",
    "PAHA": "pinnacle_asian_handicap_away_odds",
    "MAXAHH": "market_maximum_asian_handicap_home_odds",
    "MAXAHA": "market_maximum_asian_handicap_away_odds",
    "AVGAHH": "market_average_asian_handicap_home_odds",
    "AVGAPA": "market_average_asian_handicap_away_odds",
    "SYA": "stanley_bet_away_odds",
    "LBH": "lad_brokes_home_win_odds",
    "LBAHH": "lad_brokes_asian_handicap_odds",
    "BBAV>2.5": "bet_brains_average_over_2.5_goals",
    "SJA": "stan_james_away_odds",
    "BBMX<2.5": "bet_brain_maximum_under_2.5_goals",
    "LBAH": "lad_brokes_size_of_handicap_home_odds",
    "SOH": "sporting_odds_home_win_odds",
    "BSD": "blue_square_draw_odds",
    "B365AH": "bet_365_size_handicap_home_odds",
    "SOA": "sporting_wins_away_win_odds",
    "SOD": "sporting_wins_draw_odds",
    "SBD": "sporting_bet_draw_odds",
    "GBAHA": "gamebookers_asian_handicap_away_team_odds",
    "SJD": "stan_james_draw_odds",
    "GBAHH": "gamebookers_asian_handicap_home_team_odds",
    "HHW": "home_team_hit_woodwork",
    "BBAV<2.5": "bet_brain_average_under_2.5_goals_odds",
    "BBMX>2.5": "bet_brain_maximum_over_2.5_goals_odds",
    "BBAHH": "bet_brain_size_of_home_handicap",
    "BBMXAHH": "betbrain_maximum_asian_handicap_home_team_odds",
    "BSA": "blue_square_away_win_odds",
    "AHW": "away_team_hit_woodwork",
    "LBA": "lad_brokes_away_win_odds",
    "BBAVH": "bet_brain_average_home_win_odds",
    "LBD": "lad_brokes_draw_odds",
    "BBAVAHH": "bet_brain_average_asian_handicap_home_team_odds",
    "BSH": "blue_square_home_win_odds",
    "ABP": "away_team_booking_points",
    "BBMXD": "bet_brain_maximum_draw_odds",
    "GBAH": "game_bookers_size_of_handicap",
    "BBAVD": "bet_brain_average_draw_win_odds",
    "GBH": "game_bookers_home_win_odds",
    "AO": "away_team_offsides",
    "GB>2.5": "game_bookers_over_2.5_goals_odds",
    "HBP": "home_team_booking_points",
    "SYH": "stanley_bet_home_win_odds",
    "SJH": "stan_james_home_win_odds",
    "SBA": "sporting_bet_away_win_odds",
    "GB<2.5": "game_bookers_under_2.5_goals_odds",
    "HO": "home_team_offsides",
    "LBAHA": "lad_brokes_asian_handicap_away_team_odds",
    "GBD": "game_bookers_draw_odds",
    "SBH": "sporting_bet_home_win_odds",
    "BBMXA": "bet_brain_maximum_away_win_odds",
    "BBMXH": "bet_brain_maximum_home_team_odds",
    "GBA": "game_bookers_away_win_odds",
    "SYD": "stanley_bet_draw_odds",
}