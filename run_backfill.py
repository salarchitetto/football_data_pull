from configs import LeagueDictionary, TerminalColors, ascii_intro_footy, ascii_intro_dash
from utilities.postgres.postgres_utils import PostgresUtils
from utilities.id_generator import TeamIDGenerator
from utilities.logger import Logger
from utilities.process_backfill import ProcessorBackFill
from utilities.configurator import Configurator
import time

if __name__ == "__main__":
    logger = Logger(logger_name="Back Fill Data Processor")
    logger.info(f"{TerminalColors.OKCYAN}{ascii_intro_footy}{TerminalColors.ENDC}{ascii_intro_dash}")

    logger.info("Dropping table if exists results")
    PostgresUtils().execute("DROP TABLE IF EXISTS results")
    logger.info("Dropping table if exists teams")
    PostgresUtils().execute("DROP TABLE IF EXISTS teams")
    configs = Configurator()
    id_generator = TeamIDGenerator()

    for league in LeagueDictionary:
        start_time = time.time()

        logger.info(f"Starting the process for: ",
                    leage_name=league.name.lower(), excel_path=league['excel_path'], country=league['country'])
        # Running through process of ingesting CSV's
        configs.country = league['country']
        configs.file_name = league.name.lower()
        configs.league_name = league['file_name']
        configs.excel_path = league['excel_path']

        ProcessorBackFill(configs).process_back_fill(id_generator)

        logger.info(f"--- {(time.time() - start_time)} seconds ---")
        logger.info(f"{'*' * 75}")

    logger.info("Creating distinct teams table")
    PostgresUtils().execute("ALTER TABLE results ADD PRIMARY KEY (match_id);")
    PostgresUtils().create_distinct_teams_table()
    PostgresUtils().execute("ALTER TABLE teams ADD PRIMARY KEY (team_id);")
