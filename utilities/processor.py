from postgres.postgres_utils import PostgresUtils
from utilities.configurator import Configurator
from utilities.dataframe_util import DataframeUtil
from utilities.logger import Logger
from utilities.season_dates import SeasonDates


class Processor:
    def __init__(self,
                 configs: Configurator):
        self.configs = configs
        self.logger = Logger(logger_name="Processor")
        self.season_dates = SeasonDates(self.configs)

    def process(self):
        dataframe_util = DataframeUtil()
        postgres = PostgresUtils()
        path_to_csv_link = self.season_dates.get_current_season_download_path()
        season_formatted = self.season_dates.format_season_string(self.season_dates.get_this_season())

        dataframe = dataframe_util.get_dataframe(path_to_csv_link)
        dataframe = dataframe_util.add_season_to_dataframe(season_formatted, dataframe)
        cleaned_dataframe = dataframe_util.clean_dataframe(dataframe, self.configs.league_name)

        previous_run_time = postgres.get_high_water_mark_time(league_name=self.configs.league_name)
        filtered_dataframe = dataframe_util.high_water_mark_filter(cleaned_dataframe, previous_run_time)

        if filtered_dataframe.empty:
            self.logger.info("Dataframe is empty, will not attempt to write")
        else:
            postgres.upload_dataframe(filtered_dataframe)
