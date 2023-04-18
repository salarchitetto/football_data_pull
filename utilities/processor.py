from postgres.postgres_utils import PostgresUtils
from utilities.configurator import Configurator
from utilities.dataframe_util import DataframeUtil


class Processor:
    def __init__(self,
                 configs: Configurator,
                 dataframe_util: DataframeUtil):
        self.configs = configs
        self.dataframe_util = dataframe_util
        self.postgres = PostgresUtils()

    def process(self):
        path = self.configs.link_to_download_path()[0]
        dataframe = self.dataframe_util.clean_dataframe(self.dataframe_util.get_dataframe(path))

        previous_run_time = self.postgres.get_high_water_mark_time(league_name=self.configs.file_name)
        filtered_dataframe = self.dataframe_util.high_water_mark_filter(dataframe, previous_run_time)

        if filtered_dataframe.empty:
            print("Dataframe is empty, will not attempt to write")
        else:
            PostgresUtils().upload_dataframe(filtered_dataframe)
