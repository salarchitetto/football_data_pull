from configs import LeagueDictionary
from postgres.postgres_utils import PostgresUtils
from utilities.logger import Logger
from utilities.process_backfill import ProcessorBackFill
from utilities.configurator import Configurator
import time

if __name__ == "__main__":
    PostgresUtils().execute("DROP TABLE IF EXISTS results")
    configs = Configurator()

    logger = Logger(logger_name="Back Fill Data Processor")

    for league in LeagueDictionary:
        start_time = time.time()

        logger.info(f"Starting the process for: ",
                    leage_name=league.name.lower(), excel_path=league['excel_path'], country=league['country'])
        # Running through process of ingesting CSV's
        configs.country = league['country']
        configs.file_name = league.name.lower()
        configs.league_name = league['file_name']
        configs.excel_path = league['excel_path']
        ProcessorBackFill(configs, "results").process_back_fill()

        logger.info(f"--- {(time.time() - start_time)} seconds ---")
        logger.info(f"{'*' * 75}")
