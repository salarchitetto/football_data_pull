import uuid


class TeamIDGenerator:
    def __init__(self):
        self.generated_ids = {}
        self.generated_names = set()

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

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())
