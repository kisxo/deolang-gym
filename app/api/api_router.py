from fastapi import APIRouter
from app.api.v1.endpoints import users, members

router = APIRouter()

router.include_router(users.router, prefix="/v1/users", tags=["users"])
router.include_router(members.router, prefix="/v1/members", tags=["member"])