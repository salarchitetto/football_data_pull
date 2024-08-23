from configuration.configurator import Configurator
from configuration.football_data_uk_configuration import football_data_uk, FOOTBALL_DATA_UK_MAPPING
from utilities.footy_dataframes import *
from utilities.logger import Logger
from utilities.season_formatter import SeasonDates

logger: Logger = Logger("NORMAL_RUN")
# If running this for the first time change this to 25
# This will back-fill all seasons (That I can get from this source)
# Set to one to do the current season only
NUMBER_OF_SEASONS: int = 100


def main() -> None:
    for country, data in football_data_uk.items():
        for league in data.get("leagues", []):
            configurator = Configurator(conf=football_data_uk, country=country, league=league)
            logger.info(f"Setting up Configurator for {country.name} - {league.name}")
            season_dates = SeasonDates(configurator, NUMBER_OF_SEASONS)
            paths_to_process = season_dates.get_csv_download_paths()

            for path, formatted_season in zip(paths_to_process, season_dates.get_formatted_seasons_list()):
                logger.info(f"Running process for season {formatted_season}")
                dataframe = (
                    DataFrameUtilities(SourceType.EXCEL, path)
                    .clean_dataframe_depending_on_source_type()
                )
                # TODO: How do I want to handle the difference in dataframe columns?
                # OPTION 1:
                # - Should I have them store in a list, process the difference between all the columns
                # - then add missing ones to each dataframe?

                # OR

                # OPTION 2:
                # - I can use the existing dictionary (I.E: FOOTBALL_DATA_UK_MAPPING) to and see what
                # - columns exist and if some don't, add them. I think this might entail mapping out the
                # - datatypes for each column but that should be okay.

                # I like option 2. No need for lists and can work with the data as of (less memory and faster)
                print(dataframe)


if __name__ == "__main__":
    main()


main()
