from configs import Variables
from utilities.directories import Directories
from utilities.processor import Processor
from utilities.configurator import Configurator
import time

if __name__ == "__main__":
    # Creating Directories
    Directories(Variables.league_dictionary).create_footy_directories()

    for league, values in Variables.league_dictionary.items():
        start_time = time.time()

        print(f"{league} -- {values['excel_path']} -- {values['country']}")
        # Running through process of ingesting CSV's
        configs = Configurator(values['country'], league, values['excel_path'])
        Processor(configs).process()

        print("--- %s seconds ---" % (time.time() - start_time))
