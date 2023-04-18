from configs import Variables
from postgres.postgres_utils import PostgresUtils
from utilities.dataframe_util import DataframeUtil
from utilities.process_backfill import ProcessorBackFill
from utilities.configurator import Configurator
import time

if __name__ == "__main__":
    PostgresUtils().execute("DROP TABLE results")

    for league, values in Variables.league_dictionary.items():
        start_time = time.time()

        print(f"{league} -- {values['excel_path']} -- {values['country']}")
        # Running through process of ingesting CSV's
        configs = Configurator(values['country'], league, values['excel_path'], values['file_name'])
        dataframe_utils = DataframeUtil(configs)
        ProcessorBackFill(configs, dataframe_utils).process_back_fill()
        print("--- %s seconds ---" % (time.time() - start_time))
