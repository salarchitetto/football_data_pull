"""Main Method for Football Data UK."""

from datetime import datetime

from configuration.configuration_enums import SourceType
from configuration.configurator import Configurator
from configuration.football_data_uk_configuration import FOOTBALL_DATA_UK_MAPPING, football_data_uk
from postgres.postgres_utils import FootyPostgres
from utilities.footy_dataframes import dataframe_cleanser
from utilities.high_water_mark import HighWaterMarkProcessor
from utilities.logger import Logger
from utilities.season_formatter import SeasonDates
from utilities.team_uuid_generator import TeamUUIDGenerator
from utilities.utilities import TextColor, generate_create_table_query, highlight_text

# TODO: Pass in args depending on if it's the first time running or not.

logger: Logger = Logger("MAIN")
# If running this for the first time change this to 25
# This will back-fill all seasons (That I can get from this source, from 2000 onward)
# Set to one to do the current season only
NUMBER_OF_SEASONS: int = 1

# Primer Stuff
FootyPostgres().execute(
    query="""
CREATE TABLE IF NOT EXISTS teams (
    team_name VARCHAR(100) NOT NULL,
    team_id VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );"""
)

FootyPostgres().execute(
    query=generate_create_table_query("results", FOOTBALL_DATA_UK_MAPPING)
)


def main() -> None:
    """Football Data UK data processing."""
    for country, data in football_data_uk.items():
        for league in data.get("leagues"):
            logger.info(f"{'*' * 100}")
            logger.info(f"Setting up Configurator for {country.name} - {league.name}")

            configurator = Configurator(
                conf=football_data_uk, country=country, league=league
            )
            season_dates = SeasonDates(configurator, NUMBER_OF_SEASONS)
            paths_to_process = season_dates.get_csv_download_paths()

            for path, formatted_season in zip(
                paths_to_process, season_dates.get_formatted_seasons_list()
            ):
                logger.info(
                    f"Running process for season {formatted_season} - {league.name}"
                )

                process_start_time = datetime.now()

                dataframe = dataframe_cleanser(
                    SourceType.EXCEL, path, league, formatted_season
                )
                hwm = HighWaterMarkProcessor(
                    dataframe, "results", league, formatted_season
                )

                dataframe_diff = hwm.get_filtered_dataframe()

                # check if the dataframe is empty via HWM
                if dataframe_diff.is_empty():
                    logger.info(
                        "Incoming data is empty relative to HWM, proceeding to next iteration."
                    )
                    continue

                processed_dataframe = TeamUUIDGenerator(
                    dataframe_diff, "home_team", "away_team"
                ).uuid_processor()

                FootyPostgres().post_dataframe(processed_dataframe, "results")

                process_end_time = datetime.now()
                process_duration_seconds = highlight_text(
                    (process_end_time - process_start_time).total_seconds(),
                    TextColor.RED,
                )

                number_of_records_processed = highlight_text(
                    len(processed_dataframe), TextColor.GREEN
                )

                logger.info(
                    f"Inserted {number_of_records_processed} records into the results table"
                )
                logger.info(
                    f"Data written for {country.name} - {league.name} | {formatted_season}"
                )
                logger.info(
                    f"""Processing for {league.name} | {formatted_season} took:
                     {process_duration_seconds} seconds"""
                )
                logger.info(f"{'*' * 100}")
                logger.info("")


def atest(name: str) -> str:
    print(name)


if __name__ == "__main__":
    full_start_time = datetime.now()
    main()
    full_end_time = datetime.now()
    full_duration_seconds = highlight_text(
        (full_end_time - full_start_time).total_seconds(), TextColor.GREEN
    )

    logger.info(f"Full Duration of application: {full_duration_seconds} seconds.")
