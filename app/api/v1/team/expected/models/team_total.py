from pydantic import BaseModel


class TeamTotal(BaseModel):
    pts_scored: int
