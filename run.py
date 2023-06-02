from configs import LeagueDictionary, ascii_intro_footy, TerminalColors, ascii_intro_dash
from utilities.logger import Logger
from utilities.processor import Processor
from utilities.configurator import Configurator
import time

if __name__ == "__main__":

    configs = Configurator()
    logger = Logger(logger_name="Data Processor")

    logger.info(f"{TerminalColors.OKCYAN}{ascii_intro_footy}{TerminalColors.ENDC}{ascii_intro_dash}")

    for league in LeagueDictionary:
        start_time = time.time()

        logger.info("Starting the process for: ",
                    leage_name=league.name.lower(), excel_path=league['excel_path'], country=league['country'])
        # Running through process of ingesting CSV's
        configs.country = league['country']
        configs.excel_path = league['excel_path']
        configs.league_name = league['file_name']
        Processor(configs).process()
        logger.info(f"--- {(time.time() - start_time)} seconds ---")
        logger.info(f"{'*' * 75}")
