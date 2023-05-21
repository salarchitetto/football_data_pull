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

    def process(self):
        dataframe_util = DataframeUtil(self.configs)
        postgres = PostgresUtils()

        path_to_csv_link = SeasonDates(self.configs).get_current_season_download_path()

        dataframe = dataframe_util.clean_dataframe(dataframe_util.get_dataframe(path_to_csv_link))

        previous_run_time = postgres.get_high_water_mark_time(league_name=self.configs.league_name,
                                                              table_name="results")
        filtered_dataframe = dataframe_util.high_water_mark_filter(dataframe, previous_run_time)

        if filtered_dataframe.empty:
            self.logger.info("Dataframe is empty, will not attempt to write")
        else:
            postgres.upload_dataframe(filtered_dataframe, "results")
