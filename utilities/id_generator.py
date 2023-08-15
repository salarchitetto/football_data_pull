import uuid
from typing import List
import pandas as pd
from utilities.logger import Logger


class TeamIDGenerator:
    def __init__(self):
        self.generated_ids = {}
        self.generated_names = set()
        self.logger = Logger(logger_name="TeamIDGenerator")

    def generate_team_id(self, team_name: str) -> str:
        team_name = team_name.lower().strip()

        # Check if team name already exists
        if team_name in self.generated_names:
            return self.generated_ids[team_name]

        # Generate new team ID
        _id = self.generate_uuid()

        while _id in self.generated_ids.values():
            _id = str(uuid.uuid4())

        self.generated_ids[team_name] = _id
        self.generated_names.add(team_name)

        return _id

    def create_new_team_ids(self, list_of_team_names: List[str]) -> pd.DataFrame:
        self.logger.info("Generating new ID's for missing values")
        return pd.DataFrame(
            {
                "team_name": list_of_team_names,
                "team_id": [self.generate_uuid() for _ in list_of_team_names]
            }
        )

    @staticmethod
    def generate_uuid() -> str:
        return str(uuid.uuid4())
