from pydantic import BaseModel

from app.api.v1.team.expected.models.opponent_total import OpponentTotal
from app.api.v1.team.expected.models.team_advanced import TeamAdvanced
from app.api.v1.team.expected.models.team_total import TeamTotal


class TeamSeason(BaseModel):
    team_name: str
    team_advanced: TeamAdvanced
    team_total: TeamTotal
    opponent_total: OpponentTotal
