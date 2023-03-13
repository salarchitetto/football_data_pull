from typing import Dict, List
import os


class Directories:
    def __init__(self, dictionary: Dict):
        self.dictionary = dictionary
        self.file_path = "footy_dash_data"

    def create_initial_folder(self):
        os.mkdir(self.file_path)

    def create_footy_directories(self) -> None:
        try:
            print("File directory does not exist, creating them now.")
            for key, values in self.dictionary.items():
                os.makedirs(os.path.join(self.file_path, key))
        except FileExistsError as fee:
            print(f"Directories already exist! : {fee} - Continuing process")
            pass

    def file_directory_list(self) -> List[str]:
        dirs = []
        try:
            for root, directory, file in os.walk(self.file_path):
                for _file in file:
                    dirs.append(os.path.join(root, _file))
            return dirs
        except Exception as e:
            print(f"An error has occurred grabbing the locations: {e}")
