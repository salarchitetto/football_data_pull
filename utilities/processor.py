from utilities.configurator import Configurator
import pandas as pd


class Processor:
    def __init__(self, configs: Configurator):
        self.configs = configs

    @staticmethod
    def get_dataframe(path):
        return pd.read_csv(path, encoding="utf-8", on_bad_lines='skip')

    def save_dataframe(self, dataframe: pd.DataFrame, csv_name: str) -> None:
        dataframe.to_csv(f"{self.configs.get_directory}/{csv_name}")

    def process(self) -> None:
        self.configs.create_footy_directories()
        self.configs.create_years_list()
        self.configs.list_checker()
        self.configs.create_csv_names()
        download_paths = self.configs.link_to_download_path()
        print(download_paths)

        for path, csv_name in zip(download_paths, self.configs.csv_names):
            print(f"Working on grabbing data for: {path}")
            self.save_dataframe(self.get_dataframe(path), csv_name)


