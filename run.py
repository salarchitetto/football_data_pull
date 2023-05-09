from configs import LeagueDictionary
from utilities.processor import Processor
from utilities.configurator import Configurator
import time

if __name__ == "__main__":

    configs = Configurator()

    for league in LeagueDictionary:
        start_time = time.time()

        print(f"{league.name.lower()} -- {league['excel_path']} -- {league['country']}")
        # Running through process of ingesting CSV's
        configs.country = league['country']
        configs.excel_path = league['excel_path']
        configs.league_name = league['file_name']
        Processor(configs).process()
        print("--- %s seconds ---" % (time.time() - start_time))
