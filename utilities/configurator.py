import os
from typing import List
import platform
from configs import Variables


class Configurator:
    def __init__(self, country: str, league_name: str, excel_path: str):
        self.country = country
        self.league_name = league_name
        self.excel_path = excel_path
        self.download_link = "https://www.football-data.co.uk"
        self.link_constant = "mmz4281"
        self.year_end = range(23, -1, -1)
        self.year_start = range(22, -1, -1)
        self.list_of_years = []
        self.download_paths = []
        self.vars = Variables()
        self.file_path = "footy_dash_data"
        self.csv_names = []

    def __repr__(self):
        return ""

    @property
    def create_country_link(self) -> str:
        return f"{self.download_link}/{self.country}m.php"

    @property
    def get_directory(self) -> str:
        return f"{self.file_path}/{self.league_name}"

    def create_years_list(self) -> List[str]:
        return [str(x) + str(y) for x, y in zip(self.year_start, self.year_end)]

    def list_checker(self) -> None:
        for year in self.create_years_list():
            match len(year):
                case 4:
                    self.list_of_years.append(year)
                case 3:
                    self.list_of_years.append(f"0{year}")
                case 2:
                    self.list_of_years.append(f"0{year[0]}0{year[1]}")
                case _:
                    self.list_of_years.append("0001")

    def link_to_download_path(self) -> List[str]:
        for amended_year in self.list_of_years:
            self.download_paths \
                .append(f"{self.download_link}/{self.link_constant}/{amended_year}/{self.excel_path}.csv")

        return self.download_paths

    def create_csv_names(self):
        for year in self.create_years_list():
            self.csv_names.append(f"{self.league_name}_{year}.csv")
