from enum import Enum
from typing import Final


class LeagueDictionary(dict, Enum):
    PREMIER_LEAGUE = {
        "excel_path": "E0",
        "file_name": "premier_league",
        "country": "England",
    }
    CHAMPIONSHIP = {
        "excel_path": "E1",
        "file_name": "championship",
        "country": "England",
    }
    SCOT_PREM = {
        "excel_path": "SC0",
        "file_name": "scottish_premiership",
        "country": "Scotland",
    }
    SCOT_D1 = {
        "excel_path": "SC1",
        "file_name": "scottish_championship",
        "country": "Scotland",
    }
    BUNDESLIGA1 = {"excel_path": "D1", "file_name": "bundesliga", "country": "Germany"}
    BUNDESLIGA2 = {
        "excel_path": "D2",
        "file_name": "bundesliga_2",
        "country": "Germany",
    }
    SERIEA = {"excel_path": "I1", "file_name": "serie_a", "country": "Italy"}
    SERIEB = {"excel_path": "I2", "file_name": "serie_b", "country": "Italy"}
    LALIGA1 = {"excel_path": "SP1", "file_name": "la_liga", "country": "Spain"}
    LALIGA2 = {"excel_path": "SP2", "file_name": "la_liga_2", "country": "Spain"}
    FRENCH1 = {"excel_path": "F1", "file_name": "ligue_1", "country": "France"}
    FRENCH2 = {"excel_path": "F2", "file_name": "ligue_2", "country": "France"}
    NETHERLANDS = {
        "excel_path": "N1",
        "file_name": "eredivisie",
        "country": "Netherlands",
    }
    BELGIUM = {
        "excel_path": "B1",
        "file_name": "belgian_pro_league",
        "country": "Belgium",
    }
    PORTUGAL = {"excel_path": "P1", "file_name": "liga_portugal", "country": "Portugal"}


class TerminalColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


ascii_intro_footy: Final = (
    """
     _______   ______     ______   .___________.____    ____ 
    |   ____| /  __  \   /  __  \  |           |\   \  /   / 
    |  |__   |  |  |  | |  |  |  | `---|  |----` \   \/   /  
    |   __|  |  |  |  | |  |  |  |     |  |       \_    _/   
    |  |     |  `--'  | |  `--'  |     |  |         |  |     
    |__|      \______/   \______/      |__|         |__|     
                                                                                                                                                          
    """
)

ascii_intro_dash: Final = (
    """
        _______       ___           _______. __    __  
       |       \     /   \         /       ||  |  |  | 
       |  .--.  |   /  ^  \       |   (----`|  |__|  | 
       |  |  |  |  /  /_\  \       \   \    |   __   | 
       |  '--'  | /  _____  \  .----)   |   |  |  |  | 
       |_______/ /__/     \__\ |_______/    |__|  |__| 
                                            
    """
)

results_column_mapping = {
    "time": "match_time",
    "hometeam": "home_team",
    "awayteam": "away_team",
    "fthg": "full_time_home_team_goals",
    "ftag": "full_time_away_team_goals",
    "ftr": "full_time_result",
    "hthg": "half_time_home_team_goals",
    "htag": "half_time_away_team_goals",
    "htr": "half_time_result",
    "hs": "home_team_shots",
    "as": "away_team_shots",
    "hst": "home_team_shots_on_target",
    "ast": "away_team_shots_on_target",
    "hf": "home_team_fouls",
    "af": "away_team_fouls",
    "hc": "home_team_corners",
    "ac": "away_team_corners",
    "hy": "home_team_yellow_cards",
    "ay": "away_team_yellow_cards",
    "hr": "home_team_red_cards",
    "ar": "away_team_red_cards",
    "hfkc": "home_team_free_kicks",
    "afkc": "away_team_free_kicks",
    "b365h": "bet_365_home_odds",
    "b365d": "bet_365_draw_odds",
    "b365a": "bet_365_away_odds",
    "bwh": "bet_win_home_odds",
    "bwd": "bet_win_draw_odds",
    "bwa": "bet_win_away_odds",
    "iwh": "interwetten_home_odds",
    "iwd": "interwetten_draw_odds",
    "iwa": "interwetten_away_odds",
    "psh": "pinnacle_home_odds",
    "psd": "pinnacle_draw_odds",
    "psa": "pinnacle_away_odds",
    "whh": "william_hill_home_odds",
    "whd": "william_hill_draw_odds",
    "wha": "william_hill_away_odds",
    "vch": "vc_bet_home_odds",
    "vcd": "vc_bet_draw_odds",
    "vca": "vc_bet_away_odds",
    "maxh": "market_maximum_home_odds",
    "maxd": "market_maximum_draw_odds",
    "maxa": "market_maximum_away_odds",
    "avgh": "market_average_home_odds",
    "avgd": "market_average_draw_odds",
    "avga": "market_average_away_odds",
    "b365>2.5": "bet_365_over_2.5_goals",
    "b365<2.5": "bet_365_under_2.5_goals",
    "p>2.5": "pinnacle_over_2.5_goals_odds",
    "p<2.5": "pinnacle_under_2.5_goals_odds",
    "max>2.5": "market_maximum_over_2.5_goals_odds",
    "max<2.5": "market_maximum_under_2.5_goals_odds",
    "avg>2.5": "market_average_over_2.5_goals_odds",
    "avg<2.5": "market_average_under_2.5_goals_odds",
    "ahh": "market_size_of_handicap_home_odds",
    "b365ahh": "bet_365_asian_handicap_home_odds",
    "b365aha": "bet_365_asian_handicap_away_odds",
    "pahh": "pinnacle_asian_handicap_home_odds",
    "paha": "pinnacle_asian_handicap_away_odds",
    "maxahh": "market_maximum_asian_handicap_home_odds",
    "maxaha": "market_maximum_asian_handicap_away_odds",
    "avgahh": "market_average_asian_handicap_home_odds",
    "avgaha": "market_average_asian_handicap_away_odds",
    "sya": "stanley_bet_away_odds",
    "lbh": "lad_brokes_home_win_odds",
    "lbahh": "lad_brokes_asian_handicap_odds",
    "bbav>2.5": "bet_brains_average_over_2.5_goals",
    "sja": "stan_james_away_odds",
    "bbmx<2.5": "bet_brain_maximum_under_2.5_goals",
    "lbah": "lad_brokes_size_of_handicap_home_odds",
    "soh": "sporting_odds_home_win_odds",
    "bsd": "blue_square_draw_odds",
    "b365ah": "bet_365_size_handicap_home_odds",
    "soa": "sporting_wins_away_win_odds",
    "sod": "sporting_wins_draw_odds",
    "sbd": "sporting_bet_draw_odds",
    "gbaha": "gamebookers_asian_handicap_away_team_odds",
    "sjd": "stan_james_draw_odds",
    "gbahh": "gamebookers_asian_handicap_home_team_odds",
    "hhw": "home_team_hit_woodwork",
    "bbav<2.5": "bet_brain_average_under_2.5_goals_odds",
    "bbmx>2.5": "bet_brain_maximum_over_2.5_goals_odds",
    "bbahh": "bet_brain_size_of_home_handicap",
    "bbmxahh": "betbrain_maximum_asian_handicap_home_team_odds",
    "bsa": "blue_square_away_win_odds",
    "ahw": "away_team_hit_woodwork",
    "lba": "lad_brokes_away_win_odds",
    "bbavh": "bet_brain_average_home_win_odds",
    "lbd": "lad_brokes_draw_odds",
    "bbavahh": "bet_brain_average_asian_handicap_home_team_odds",
    "bsh": "blue_square_home_win_odds",
    "abp": "away_team_booking_points",
    "bbmxd": "bet_brain_maximum_draw_odds",
    "gbah": "game_bookers_size_of_handicap",
    "bbavd": "bet_brain_average_draw_win_odds",
    "gbh": "game_bookers_home_win_odds",
    "ao": "away_team_offsides",
    "gb>2.5": "game_bookers_over_2.5_goals_odds",
    "hbp": "home_team_booking_points",
    "syh": "stanley_bet_home_win_odds",
    "sjh": "stan_james_home_win_odds",
    "sba": "sporting_bet_away_win_odds",
    "gb<2.5": "game_bookers_under_2.5_goals_odds",
    "ho": "home_team_offsides",
    "lbaha": "lad_brokes_asian_handicap_away_team_odds",
    "gbd": "game_bookers_draw_odds",
    "sbh": "sporting_bet_home_win_odds",
    "bbmxa": "bet_brain_maximum_away_win_odds",
    "bbmxh": "bet_brain_maximum_home_team_odds",
    "gba": "game_bookers_away_win_odds",
    "syd": "stanley_bet_draw_odds",
}
