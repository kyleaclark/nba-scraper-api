from pydantic import BaseModel


class TeamSummary(BaseModel):
    name: str
    wins: str
    losses: str
    pts_scored: str
    pts_allowed: str
