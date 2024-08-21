from typing import List, Final


from utilities.logger import Logger


class Configurator:
    def __init__(self):
        self.country = None
        self.league_name = None
        self.excel_path = None
        self.file_name = None
        self.download_link: Final = "https://www.football-data.co.uk"
        self.link_constant: Final = "mmz4281"
        self.logger = Logger(logger_name="Configurator")

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def excel_path(self):
        return self._excel_path

    @excel_path.setter
    def excel_path(self, value):
        self._excel_path = value

    @property
    def league_name(self):
        return self._league_name

    @league_name.setter
    def league_name(self, value):
        self._league_name = value

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def create_country_link(self) -> str:
        return f"{self.download_link}/{self.country}m.php"

    @staticmethod
    def find_diff_between_lists(list1: List[str], list2: List[str]) -> List[str]:
        return list(set(list1) - set(list2))
