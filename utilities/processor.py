from utilities.id_generator import TeamIDGenerator
from utilities.postgres.postgres_utils import PostgresUtils
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
        self.dataframe_util = DataframeUtil()
        self.postgres_util = PostgresUtils()
        self.id_generator = TeamIDGenerator()

    def process(self):
        path_to_csv_link = self.season_dates.get_current_season_download_path()
        season_formatted = self.season_dates.format_season_string(self.season_dates.get_this_season())

        dataframe = self.dataframe_util.get_dataframe(path_to_csv_link)
        dataframe = self.dataframe_util.add_season_to_dataframe(season_formatted, dataframe)
        cleaned_dataframe = self.dataframe_util.clean_dataframe(dataframe, self.configs.league_name)

        # TODO: This should be it's own class I think
        # Check for existing ID's or New ID's to add
        unique_ids = self.dataframe_util.get_unique_teams(cleaned_dataframe)
        existing_ids = self.postgres_util.get_existing_team_ids(unique_ids)

        # Find and Add new ID's
        missing_teams = self.configs.find_diff_between_lists(unique_ids, existing_ids["team_name"].tolist())
        if len(missing_teams) > 0:
            missing_id_df = self.id_generator.create_new_team_ids(missing_teams)
            # Write missing data
            (PostgresUtils(table_name="teams")
             .upload_dataframe(dataframe=missing_id_df,
                               msg=f"Creating IDs for: {missing_teams}"))

            merged_data = self.dataframe_util.join_incoming_ids(incoming_dataframe=cleaned_dataframe,
                                                                existing_ids=existing_ids,
                                                                missing_ids=missing_id_df)
        else:
            merged_data = self.dataframe_util.join_incoming_ids(incoming_dataframe=cleaned_dataframe,
                                                                existing_ids=existing_ids)

        previous_run_time = self.postgres_util.get_high_water_mark_time(league_name=self.configs.league_name)
        filtered_dataframe = self.dataframe_util.high_water_mark_filter(merged_data, previous_run_time)

        # This needs to be better...
        filtered_dataframe["match_id"] = [self.id_generator.generate_uuid() for _ in range(len(filtered_dataframe))]

        if filtered_dataframe.empty:
            self.logger.info("Dataframe is empty, will not attempt to write")
        else:
            self.postgres_util.upload_dataframe(dataframe=filtered_dataframe,
                                                msg=f"{self.configs.league_name} : {season_formatted}"
                                                )
