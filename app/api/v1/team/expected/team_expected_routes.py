from typing import Union

import pandas as pd
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.api.v1.team.expected.team_expected_models import TeamExpectedGetResModel
from app.api.v1.team.expected.services.orchestrator import orchestrate_team_expected

router = APIRouter()


@router.get('/team/expected', response_model=Union[TeamExpectedGetResModel, BaseModel])
async def get(season_year: int, return_as_csv: bool = False):
    team_expected_data = orchestrate_team_expected(season_year)

    if return_as_csv:
        team_expected_df = pd.DataFrame(jsonable_encoder(list(team_expected_data.values())))

        export_media_type = 'text/csv'
        export_headers = {'Content-Disposition': 'attachment; filename=scraper.csv'}
        result = StreamingResponse(iter([team_expected_df.to_csv(index=False)]),
                                   headers=export_headers,
                                   media_type=export_media_type)
    else:
        result = TeamExpectedGetResModel(season_year=season_year, team_expected=team_expected_data)

    return result
