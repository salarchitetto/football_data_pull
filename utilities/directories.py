from typing import Dict
import os


class Directories:
    def __init__(self, dictionary: Dict):
        self.dictionary = dictionary
        self.file_path = "footy_dash_data"

    def create_initial_folder(self):
        os.mkdir(self.file_path)

    def create_footy_directories(self) -> None:
        for key, values in self.dictionary.items():
            os.makedirs(os.path.join(self.file_path, key))
