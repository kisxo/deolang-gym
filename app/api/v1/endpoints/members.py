from fastapi import APIRouter, HTTPException, Response
from app.db.session import SessionDep
from app.db.models.member import Members
from app.db.schemas.member import MembersPublic, MemberCreate, MemberPublic
from sqlalchemy import select
from pathlib import Path

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

@router.post("/",
    response_model= MemberPublic,
    status_code=201,
    description=Path('app/openapi_docs/api/api_v1_post_members_MemberCreate.md').read_text()
)
async def create_member(
    session: SessionDep,
    input_data: MemberCreate,
    response: Response
):
    new_member = Members(**input_data.model_dump())
    try:
        session.add(new_member)
        session.commit()
        session.refresh(new_member)
    except:
        raise HTTPException(status_code=400, detail="Something went wrong!")

    return new_member