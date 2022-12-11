from pydantic import BaseModel


class OpponentTotal(BaseModel):
    pts_allowed: int
