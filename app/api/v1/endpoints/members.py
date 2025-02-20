from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_members():
    return {"status":"true", "message": "Members"}