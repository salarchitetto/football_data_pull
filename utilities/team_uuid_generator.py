"""Team UUID Generator Module."""

import uuid
from datetime import datetime
from typing import List

import polars as pl

from postgres.postgres_utils import FootyPostgres
from utilities.footy_dataframes import get_unique_team_names
from utilities.logger import Logger
from utilities.utilities import TextColor, highlight_text


class TeamUUIDGenerator:
    """Generates a specific UUID for any given team in a Dataframe."""

    def __init__(self, dataframe: pl.DataFrame, home_team: str, away_team: str) -> None:
        self.dataframe = dataframe
        self.home_team = home_team
        self.away_team = away_team
        self.table_name = "teams"
        self.now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.generated_ids = {}
        self.postgres = FootyPostgres()
        self.logger = Logger(logger_name="TeamIDGenerator")

    def generate_team_id(self, team_name: str) -> str:
        """Generate a unique UUID for a team if it hasn't
        been assigned one yet.
        """
        team_name = team_name.lower().strip()

        # Check if team already has an assigned ID
        if team_name in self.generated_ids:
            return self.generated_ids[team_name]

        # Generate a new UUID
        _id = self.generate_uuid()
        while _id in self.generated_ids.values():
            _id = self.generate_uuid()

        self.generated_ids[team_name] = _id
        return _id

    def uuid_processor(self) -> pl.DataFrame:
        """
        Generates or retrieves UUIDs for all unique teams in the dataset.
        Returns a DataFrame with team names and corresponding UUIDs.
        """
        # The entire unique set of team_names from the incoming Dataframe.
        team_names = get_unique_team_names(
            self.dataframe, self.home_team, self.away_team
        )

        query = f"""
            SELECT team_name, team_id FROM {self.table_name}
            WHERE team_name IN ({','.join(self.add_quotes(team_names, True))})
        """

        # What we have that exists in the Database so far.
        existing_teams = self.postgres.fetch_dataframe(query)

        existing_teams_list = existing_teams.select("team_name").to_series().to_list()

        # The difference between the incoming dataframe, and what we've got in the DB.
        team_difference = list(set(team_names) - set(existing_teams_list))

        if len(team_difference) > 0:
            team_difference_dataframe = pl.DataFrame(
                {
                    "team_name": team_difference,
                    "team_id": [
                        self.generate_team_id(team) for team in team_difference
                    ],
                    "created_at": self.now,
                    "updated_at": self.now,
                }
            )
            self.postgres.post_dataframe(team_difference_dataframe, self.table_name)
            number_of_records_processed = highlight_text(
                len(team_difference_dataframe), TextColor.RED
            )
            self.logger.info(
                f"Number of new UUID's generated: {number_of_records_processed}"
            )

        # find the difference, if there is a difference write those up to the DB.
        for team in existing_teams.rows():
            self.generated_ids[team[0]] = team[1]

        return self.dataframe.pipe(self.add_match_uuid).pipe(
            self.add_home_away_team_uuid
        )

    def add_match_uuid(self, dataframe: pl.DataFrame):
        """Add a match UUID for each row in the dataframe.

        :return: Polars Dataframe with match UUIDs.
        """
        # Generate a list of UUIDs for each row in the dataframe
        uuid_series = [self.generate_uuid() for _ in range(dataframe.height)]

        # Add a new column 'match_uuid' with the generated UUIDs
        return dataframe.with_columns(
            pl.Series("match_uuid", uuid_series).alias("match_uuid")
        )

    def add_home_away_team_uuid(self, dataframe: pl.DataFrame):
        """
        Add home and away team UUIDs to the dataframe by joining the generated team IDs.

        :return: Updated dataframe with home_uuid and away_uuid columns.
        """
        # Create mapping DataFrame from the generated_ids dictionary
        mapping_data = pl.DataFrame(
            {
                "team_name": list(self.generated_ids.keys()),
                "team_id": list(self.generated_ids.values()),
            }
        )

        return (
            dataframe.drop(["home_uuid", "away_uuid"])
            .join(mapping_data, left_on="home_team", right_on="team_name")
            .rename({"team_id": "home_uuid"})
            .join(mapping_data, left_on="away_team", right_on="team_name")
            .rename({"team_id": "away_uuid"})
        )

    @staticmethod
    def add_quotes(lst: List[str], single_quote: bool = None) -> List[str]:
        """String manipulation to add quotes to a list of strings."""
        if single_quote:
            return [f"'{item}'" for item in lst]
        else:
            return [f'"{item}"' for item in lst]

    @staticmethod
    def generate_uuid() -> str:
        """Generate a UUID."""
        return str(uuid.uuid4())
