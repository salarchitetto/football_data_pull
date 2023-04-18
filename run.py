from configs import Variables
from utilities.dataframe_util import DataframeUtil
from utilities.processor import Processor
from utilities.configurator import Configurator
import time

if __name__ == "__main__":

    for league, values in Variables.league_dictionary.items():
        start_time = time.time()

        print(f"{league} -- {values['excel_path']} -- {values['country']}")
        # Running through process of ingesting CSV's
        configs = Configurator(values['country'], league, values['excel_path'], values['file_name'])
        dataframe_utils = DataframeUtil(configs)
        Processor(configs, dataframe_utils).process()
        print("--- %s seconds ---" % (time.time() - start_time))
