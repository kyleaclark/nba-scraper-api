from pydantic import BaseModel

from app.api.v1.team.expected.models.pythagorean_wins import PythagoreanWins


class TeamExpected(BaseModel):
    name: str
    wins: int
    losses: int
    record: str
    morey_pythagorean: PythagoreanWins
    hollinger_pythagorean: PythagoreanWins
