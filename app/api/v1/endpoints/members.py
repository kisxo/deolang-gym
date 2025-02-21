from fastapi import APIRouter
from app.db.session import SessionDep
from app.db.models.member import Members
from app.db.schemas.member import MembersPublic
from sqlalchemy import select

router = APIRouter()

@router.get("/",
    response_model=MembersPublic
)
async def list_members(session: SessionDep):
    """
    Returns a list of member object.\n
    Each member object contains
    1. Member id
    2. Member name
    3. member gender
    4. Member phone
    """
    statement = select(Members.member_id, Members.member_name, Members.member_gender, Members.member_phone)
    # used mapping to resolve type-error caused due to use of enums
    result = session.execute(statement).mappings().all()

    return {'data': result}