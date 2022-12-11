from pydantic import BaseModel

from app.api.v1.team.expected.models.team_expected import TeamExpected


class TeamExpectedGetResModel(BaseModel):
    season_year: int
    team_expected: dict[str, TeamExpected]
