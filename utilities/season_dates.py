from typing import List

from utilities.configurator import Configurator


class SeasonDates:
    def __init__(self, configs: Configurator):
        self.configs = configs
        self.year_end = range(23, -1, -1)
        self.year_start = range(22, -1, -1)

    def get_years_list(self) -> List[str]:
        return [str(x) + str(y) for x, y in zip(self.year_start, self.year_end)]

    def get_this_season(self) -> str:
        return self.get_years_list()[0]

    def get_seasons_list(self, season_list: List[str] = None) -> List[str]:
        if season_list:
            years_list = season_list
        else:
            years_list = self.get_years_list()

        list_of_years = []
        for year in years_list:
            match len(year):
                case 4:
                    list_of_years.append(year)
                case 3:
                    list_of_years.append(f"0{year}")
                case 2:
                    list_of_years.append(f"0{year[0]}0{year[1]}")
                case _:
                    list_of_years.append("0001")

        return list_of_years

    def get_formatted_seasons_list(self) -> List[str]:
        return [self.format_season_string(date) for date in self.get_seasons_list()]

    @staticmethod
    def format_season_string(date: str) -> str:
        return f"{date[:2]}/{date[2:]}"

    def get_current_season_download_path(self) -> str:
        return f"{self.configs.download_link}/{self.configs.link_constant}/{self.get_this_season()}/{self.configs.excel_path}.csv"

    def get_multiple_season_download_paths(self, season_list: List[str] = None) -> List[str]:
        if season_list:
            seasons_list = season_list
        else:
            seasons_list = self.get_seasons_list()

        download_paths = []

        for amended_year in seasons_list:
            download_paths.append(
                f"{self.configs.download_link}/{self.configs.link_constant}/{amended_year}/{self.configs.excel_path}.csv")

        return download_paths


