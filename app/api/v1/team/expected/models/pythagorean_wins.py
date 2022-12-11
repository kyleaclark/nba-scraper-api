from pydantic import BaseModel


class PythagoreanWins(BaseModel):
    expected_record: str
    win_rate: float
    win_percentage: float
    win_diff: int
    win_diff_formatted: str
