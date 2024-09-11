"""
football_data_uk configuration dictionary.
"""
from datetime import datetime

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
    "Time": {"mapped_column_name": "match_time", "column_type": str},
    "Date": {"mapped_column_name": "date", "column_type": datetime},
    "HomeTeam": {"mapped_column_name": "home_team", "column_type": str},
    "AwayTeam": {"mapped_column_name": "away_team", "column_type": str},
    "FTHG": {"mapped_column_name": "full_time_home_team_goals", "column_type": int},
    "FTAG": {"mapped_column_name": "full_time_away_team_goals", "column_type": int},
    "FTR": {"mapped_column_name": "full_time_result", "column_type": str},
    "HTHG": {"mapped_column_name": "half_time_home_team_goals", "column_type": int},
    "HTAG": {"mapped_column_name": "half_time_away_team_goals", "column_type": int},
    "HTR": {"mapped_column_name": "half_time_result", "column_type": str},
    "HS": {"mapped_column_name": "home_team_shots", "column_type": int},
    "AS": {"mapped_column_name": "away_team_shots", "column_type": int},
    "HST": {"mapped_column_name": "home_team_shots_on_target", "column_type": int},
    "AST": {"mapped_column_name": "away_team_shots_on_target", "column_type": int},
    "HF": {"mapped_column_name": "home_team_fouls", "column_type": int},
    "AF": {"mapped_column_name": "away_team_fouls", "column_type": int},
    "HC": {"mapped_column_name": "home_team_corners", "column_type": int},
    "AC": {"mapped_column_name": "away_team_corners", "column_type": int},
    "HY": {"mapped_column_name": "home_team_yellow_cards", "column_type": int},
    "AY": {"mapped_column_name": "away_team_yellow_cards", "column_type": int},
    "HR": {"mapped_column_name": "home_team_red_cards", "column_type": int},
    "AR": {"mapped_column_name": "away_team_red_cards", "column_type": int},
    "Div": {"mapped_column_name": "league_name", "column_type": str},
    "HFKC": {"mapped_column_name": "home_team_free_kicks", "column_type": int},
    "AFKC": {"mapped_column_name": "away_team_free_kicks", "column_type": int},
    "B365H": {"mapped_column_name": "bet_365_home_odds", "column_type": float},
    "B365D": {"mapped_column_name": "bet_365_draw_odds", "column_type": float},
    "B365A": {"mapped_column_name": "bet_365_away_odds", "column_type": float},
    "BWH": {"mapped_column_name": "bet_win_home_odds", "column_type": float},
    "BWD": {"mapped_column_name": "bet_win_draw_odds", "column_type": float},
    "BWA": {"mapped_column_name": "bet_win_away_odds", "column_type": float},
    "IWH": {"mapped_column_name": "interwetten_home_odds", "column_type": float},
    "IWD": {"mapped_column_name": "interwetten_draw_odds", "column_type": float},
    "IWA": {"mapped_column_name": "interwetten_away_odds", "column_type": float},
    "PSH": {"mapped_column_name": "pinnacle_home_odds", "column_type": float},
    "PSD": {"mapped_column_name": "pinnacle_draw_odds", "column_type": float},
    "PSA": {"mapped_column_name": "pinnacle_away_odds", "column_type": float},
    "WHH": {"mapped_column_name": "william_hill_home_odds", "column_type": float},
    "WHD": {"mapped_column_name": "william_hill_draw_odds", "column_type": float},
    "WHA": {"mapped_column_name": "william_hill_away_odds", "column_type": float},
    "VCH": {"mapped_column_name": "vc_bet_home_odds", "column_type": float},
    "VCD": {"mapped_column_name": "vc_bet_draw_odds", "column_type": float},
    "VCA": {"mapped_column_name": "vc_bet_away_odds", "column_type": float},
    "MAXH": {"mapped_column_name": "market_maximum_home_odds", "column_type": float},
    "MAXD": {"mapped_column_name": "market_maximum_draw_odds", "column_type": float},
    "MAXA": {"mapped_column_name": "market_maximum_away_odds", "column_type": float},
    "AVGH": {"mapped_column_name": "market_average_home_odds", "column_type": float},
    "AVGD": {"mapped_column_name": "market_average_draw_odds", "column_type": float},
    "AVGA": {"mapped_column_name": "market_average_away_odds", "column_type": float},
    "B365>2.5": {"mapped_column_name": "bet_365_over_2_5_goals", "column_type": float},
    "B365<2.5": {"mapped_column_name": "bet_365_under_2_5_goals", "column_type": float},
    "P>2.5": {"mapped_column_name": "pinnacle_over_2_5_goals_odds", "column_type": float},
    "P<2.5": {"mapped_column_name": "pinnacle_under_2_5_goals_odds", "column_type": float},
    "MAX>2.5": {"mapped_column_name": "market_maximum_over_2_5_goals_odds", "column_type": float},
    "MAX<2.5": {"mapped_column_name": "market_maximum_under_2_5_goals_odds", "column_type": float},
    "AVG>2.5": {"mapped_column_name": "market_average_over_2_5_goals_odds", "column_type": float},
    "AVG<2.5": {"mapped_column_name": "market_average_under_2_5_goals_odds", "column_type": float},
    "AHH": {"mapped_column_name": "market_size_of_handicap_home_odds", "column_type": float},
    "B365AHH": {"mapped_column_name": "bet_365_asian_handicap_home_odds", "column_type": float},
    "B365AHA": {"mapped_column_name": "bet_365_asian_handicap_away_odds", "column_type": float},
    "PAHH": {"mapped_column_name": "pinnacle_asian_handicap_home_odds", "column_type": float},
    "PAHA": {"mapped_column_name": "pinnacle_asian_handicap_away_odds", "column_type": float},
    "MAXAHH": {"mapped_column_name": "market_maximum_asian_handicap_home_odds", "column_type": float},
    "MAXAHA": {"mapped_column_name": "market_maximum_asian_handicap_away_odds", "column_type": float},
    "AVGAHH": {"mapped_column_name": "market_average_asian_handicap_home_odds", "column_type": float},
    "AVGAPA": {"mapped_column_name": "market_average_asian_handicap_away_odds", "column_type": float},
    "SYA": {"mapped_column_name": "stanley_bet_away_odds", "column_type": float},
    "LBH": {"mapped_column_name": "lad_brokes_home_win_odds", "column_type": float},
    "LBAHH": {"mapped_column_name": "lad_brokes_asian_handicap_odds", "column_type": float},
    "BBAV>2.5": {"mapped_column_name": "bet_brains_average_over_2_5_goals", "column_type": float},
    "SJA": {"mapped_column_name": "stan_james_away_odds", "column_type": float},
    "BBMX<2.5": {"mapped_column_name": "bet_brain_maximum_under_2_5_goals", "column_type": float},
    "LBAH": {"mapped_column_name": "lad_brokes_size_of_handicap_home_odds", "column_type": float},
    "SOH": {"mapped_column_name": "sporting_odds_home_win_odds", "column_type": float},
    "BSD": {"mapped_column_name": "blue_square_draw_odds", "column_type": float},
    "B365AH": {"mapped_column_name": "bet_365_size_handicap_home_odds", "column_type": float},
    "SOA": {"mapped_column_name": "sporting_wins_away_win_odds", "column_type": float},
    "SOD": {"mapped_column_name": "sporting_wins_draw_odds", "column_type": float},
    "SBD": {"mapped_column_name": "sporting_bet_draw_odds", "column_type": float},
    "GBAHA": {"mapped_column_name": "gamebookers_asian_handicap_away_team_odds", "column_type": float},
    "SJD": {"mapped_column_name": "stan_james_draw_odds", "column_type": float},
    "GBAHH": {"mapped_column_name": "gamebookers_asian_handicap_home_team_odds", "column_type": float},
    "HHW": {"mapped_column_name": "home_team_hit_woodwork", "column_type": int},
    "BBAV<2.5": {"mapped_column_name": "bet_brain_average_under_2_5_goals_odds", "column_type": float},
    "BBMX>2.5": {"mapped_column_name": "bet_brain_maximum_over_2_5_goals_odds", "column_type": float},
    "BBAHH": {"mapped_column_name": "bet_brain_size_of_home_handicap", "column_type": float},
    "BBMXAHH": {"mapped_column_name": "betbrain_maximum_asian_handicap_home_team_odds", "column_type": float},
    "BSA": {"mapped_column_name": "blue_square_away_win_odds", "column_type": float},
    "AHW": {"mapped_column_name": "away_team_hit_woodwork", "column_type": int},
    "LBA": {"mapped_column_name": "lad_brokes_away_win_odds", "column_type": float},
    "BBAVH": {"mapped_column_name": "bet_brain_average_home_win_odds", "column_type": float},
    "LBD": {"mapped_column_name": "lad_brokes_draw_odds", "column_type": float},
    "BBAVAHH": {"mapped_column_name": "bet_brain_average_asian_handicap_home_team_odds", "column_type": float},
    "BSH": {"mapped_column_name": "blue_square_home_win_odds", "column_type": float},
    "ABP": {"mapped_column_name": "away_team_booking_points", "column_type": int},
    "BBMXD": {"mapped_column_name": "bet_brain_maximum_draw_odds", "column_type": float},
    "GBAH": {"mapped_column_name": "game_bookers_size_of_handicap", "column_type": float},
    "BBAVD": {"mapped_column_name": "bet_brain_average_draw_win_odds", "column_type": float},
    "GBH": {"mapped_column_name": "game_bookers_home_win_odds", "column_type": float},
    "AO": {"mapped_column_name": "away_team_offsides", "column_type": int},
    "GB>2.5": {"mapped_column_name": "game_bookers_over_2_5_goals_odds", "column_type": float},
    "HBP": {"mapped_column_name": "home_team_booking_points", "column_type": int},
    "SYH": {"mapped_column_name": "stanley_bet_home_win_odds", "column_type": float},
    "SJH": {"mapped_column_name": "stan_james_home_win_odds", "column_type": float},
    "SBA": {"mapped_column_name": "sporting_bet_away_win_odds", "column_type": float},
    "GB<2.5": {"mapped_column_name": "game_bookers_under_2_5_goals_odds", "column_type": float},
    "HO": {"mapped_column_name": "home_team_offsides", "column_type": int},
    "LBAHA": {"mapped_column_name": "lad_brokes_asian_handicap_away_team_odds", "column_type": float},
    "GBD": {"mapped_column_name": "game_bookers_draw_odds", "column_type": float},
    "SBH": {"mapped_column_name": "sporting_bet_home_win_odds", "column_type": float},
    "BBMXA": {"mapped_column_name": "bet_brain_maximum_away_win_odds", "column_type": float},
    "BBMXH": {"mapped_column_name": "bet_brain_maximum_home_team_odds", "column_type": float},
    "GBA": {"mapped_column_name": "game_bookers_away_win_odds", "column_type": float},
    "SYD": {"mapped_column_name": "stanley_bet_draw_odds", "column_type": float},
    "high_water_mark": {"mapped_column_name": "high_water_mark", "column_type": datetime},
    "season": {"mapped_column_name": "season", "column_type": str},
    "home_uuid": {"mapped_column_name": "home_uuid", "column_type": str},
    "away_uuid": {"mapped_column_name": "away_uuid", "column_type": str},
    "match_uuid": {"mapped_column_name": "match_uuid", "column_type": str}
}
