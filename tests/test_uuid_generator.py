import unittest
import polars as pl

from utilities.team_uuid_generator import TeamUUIDGenerator


class TestUUIDGenerator(unittest.TestCase):
    """
    """

    def setUp(self) -> None:
        self.test_dataframe = pl.DataFrame({
                "team_names": ["juventus", "arsenal", "bayern_munich"],
                "team_id": [None, None, None]  # Empty team_id column
            })
        self.uuid_generator = TeamUUIDGenerator(self.test_dataframe, "home_team", "away_team")

    def test_uuid_generator(self):
        """

        :return:
        """
        print(self.uuid_generator.generate_team_id("juventus"))
        print(self.uuid_generator.generate_team_id("juventus"))
        print(self.uuid_generator.generate_team_id("arsenal"))
        print(self.uuid_generator.generated_ids)
