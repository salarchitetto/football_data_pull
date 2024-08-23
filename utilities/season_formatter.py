from datetime import datetime
from typing import List

from configuration.configurator import Configurator
from utilities.logger import Logger


class SeasonDates:
    """
    The SeasonDates class is responsible for generating and formatting football season date strings based on the current year.
    It also provides methods to retrieve season-specific download paths for CSV files based on the configuration provided.

    Attributes:
        configs (Configurator): An instance of the Configurator class containing the configuration for the country and league.
        current_year (int): The current year in two-digit format (e.g., 24 for 2024).
        year_end (List[int]): A list of years representing the end year of each season, starting from the next year down to zero.
        year_start (List[int]): A list of years representing the start year of each season, starting from the current year down to zero.
        number_of_seasons (int): The number of seasons to be considered, which determines how many season date strings are generated.
    """

    def __init__(self, configs: Configurator, number_of_seasons: int = 1):
        """
        Initializes the SeasonDates instance with the given configuration and number of seasons.
        
        :param configs: An instance of the Configurator class containing configuration data.
        :param number_of_seasons: The number of seasons to consider when generating season date strings.
        """
        self.configs = configs
        self.current_year = datetime.now().year % 100
        self.year_end = list(range(self.current_year + 1, -1, -1))
        self.year_start = list(range(self.current_year, -1, -1))
        self.number_of_seasons = number_of_seasons
        self.logger = Logger(SeasonDates.__name__)

    @property
    def number_of_seasons(self) -> int:
        """
        Returns the number of seasons being considered.

        :return: The number of seasons.
        """
        return self._number_of_seasons

    @number_of_seasons.setter
    def number_of_seasons(self, value: int):
        """
        Sets the number of seasons to consider when generating season date strings.
        
        :param value: The number of seasons.
        """
        assert value > 0, self.logger.error("Value must be greater than 0.")
        self._number_of_seasons = value

    @property
    def seasons(self) -> List[str]:
        """
        Generates a list of season date strings based on the current year.

        :return: A list of season date strings in the format "YYNN", where YY is the start year and NN is the end year.
        """
        return [str(x) + str(y) for x, y in zip(self.year_start, self.year_end)][:self._number_of_seasons]

    @property
    def current_season(self) -> str:
        """
        Returns the current football season date string in the format "YYNN".

        :return: The current season date string.
        """
        return f"{self.year_start[0]}{self.year_end[0]}"

    def formatted_season_list(self) -> List[str]:
        """
        Formats the list of season date strings into a four-digit format.

        :return: A list of formatted season date strings in four-digit format, suitable for CSV download paths.
        """

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
        """
        Formats the list of season date strings into "YY-NN" format.

        :return: A list of formatted season date strings in "YY-NN" format.
        """
        return [f"{date[:2]}-{date[2:]}" for date in self.formatted_season_list()]

    def get_csv_download_paths(self) -> List[str]:
        """
        Generates a list of URLs for downloading season-specific CSV files based on the league and configuration.

        :return: A list of URLs for downloading CSV files corresponding to each season.
        """
        return [
            f"{self.configs.excel_link}/{year}/{self.configs.excel_identifier}.csv"
            for year in self.formatted_season_list()
        ]
