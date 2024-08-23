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