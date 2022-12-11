from fastapi.routing import APIRouter

from app.api.v1.liveness.liveness_routes import router as liveness_router
from app.api.v1.readiness.readiness_routes import router as readiness_router
from app.api.v1.team.expected.team_expected_routes import router as team_expected


api_router = APIRouter()

api_router.include_router(liveness_router, prefix='/api/v1', tags=['liveness'])
api_router.include_router(readiness_router, prefix='/api/v1', tags=['readiness'])
api_router.include_router(team_expected, prefix='/api/v1', tags=['team_expected'])
