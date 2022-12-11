from pydantic import BaseModel


class TeamAdvanced(BaseModel):
    wins: int
    losses: int
