from configs import LeagueDictionary
from postgres.postgres_utils import PostgresUtils
from utilities.process_backfill import ProcessorBackFill
from utilities.configurator import Configurator
import time

if __name__ == "__main__":
    PostgresUtils().execute("DROP TABLE IF EXISTS results")
    configs = Configurator()

    for league in LeagueDictionary:
        start_time = time.time()

        print(f"{league.name.lower()} -- {league['excel_path']} -- {league['country']}")
        # Running through process of ingesting CSV's
        configs.country = league['country']
        configs.league_name = league.name.lower()
        configs.excel_path = league['excel_path']
        configs.file_name = league['file_name']
        ProcessorBackFill(configs, "results").process_back_fill()
        print("--- %s seconds ---" % (time.time() - start_time))
