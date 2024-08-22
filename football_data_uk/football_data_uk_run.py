# from .configuration.football_data_uk_configuration import football_data_uk
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from configuration.football_data_uk_configuration import football_data_uk
from football_data_uk.season_formatter import SeasonDates
from utilities.logger import Logger
from configuration.configurator import Configurator

logger = Logger("NORMAL_RUN")
# TODO: check limit, we should be able to pass in 1 or 20
#  if its set to one it should run the most recent season, if not just run the selected limit amount.


def main() -> None:
    for country, data in football_data_uk.items():
        for league in data.get("leagues", []):
            configurator = Configurator(conf=football_data_uk, country=country, league=league)
            season_dates = SeasonDates(configurator, 2)
            logger.info(f"Configurator for {country.name} - {league.name}")
            # logger.info(configurator.excel_link)
            logger.info(season_dates.get_multiple_season_download_paths())


main()
