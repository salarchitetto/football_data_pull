from datetime import datetime
from typing import List

from configuration.configuration_enums import SourceType
from configuration.configurator import Configurator


class SeasonDates:
    """
    A way to map out football data uk's season dates.
    """

    def __init__(self, configs: Configurator, number_of_seasons: int = None):
        self.configs = configs
        self.current_year = datetime.now().year % 100
        self.year_end = list(range(self.current_year + 1, -1, -1))
        self.year_start = list(range(self.current_year, -1, -1))
        self.number_of_seasons = number_of_seasons

    @property
    def number_of_seasons(self) -> int:
        return self._number_of_seasons

    @number_of_seasons.setter
    def number_of_seasons(self, value):
        self._number_of_seasons = value

    @property
    def seasons(self) -> List[str]:
        season_list = [str(x) + str(y) for x, y in zip(self.year_start, self.year_end)]
        if self.number_of_seasons:
            return season_list[:self.number_of_seasons]
        else:
            return season_list

    @property
    def current_season(self) -> str:
        return f"{self.year_start[0]}{self.year_end[0]}"

    def formatted_season_list(self) -> List[str]:
        def year_formatter(year: str) -> str:
            match len(year):
                case 4:
                    return year
                case 3:
                    return f"0{year}"
                case 2:
                    return f"0{year[0]}0{year[1]}"
                case _:
                    return "0001"

        return [year_formatter(year) for year in self.seasons]

    def get_formatted_seasons_list(self) -> List[str]:
        return [self.format_season_string(date) for date in self.formatted_season_list()]

    def get_current_season_download_path(self) -> str:
        if self.configs.source_type == SourceType.EXCEL:
            return f"{self.configs.excel_link}/{self.current_season}/{self.configs.excel_identifier}.csv"
        raise ValueError(f"Source type {self.configs.source_type} not supported at this time")

    def get_multiple_season_download_paths(self) -> List[str]:
        return [
            f"{self.configs.excel_link}/{year}/{self.configs.excel_identifier}.csv"
            for year in self.formatted_season_list()
        ]

    @staticmethod
    def format_season_string(date: str) -> str:
        return f"{date[:2]}-{date[2:]}"
