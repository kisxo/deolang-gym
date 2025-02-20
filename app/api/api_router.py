from fastapi import APIRouter
from app.api.v1.endpoints import members

router = APIRouter()

router.include_router(members.router, prefix="/v1/members", tags=["member"])