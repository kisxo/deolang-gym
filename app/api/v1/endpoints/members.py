from fastapi import APIRouter, HTTPException, Response, Depends
from app.db.session import SessionDep
from app.db.models.member import Members
from app.db.schemas.member import MembersPublic, MemberCreate, MemberPublic
from sqlalchemy import select
from pathlib import Path
from app.core.security import security

router = APIRouter()

@router.get("/",
    response_model=MembersPublic,
    description=Path('app/openapi_docs/api/v1/get_members.md').read_text(),
    dependencies=[Depends(security.access_token_required)]
)
async def list_members(session: SessionDep):
    statement = select(Members.member_id, Members.member_name, Members.member_gender, Members.member_phone)
    # used mapping to resolve type-error caused due to use of enums
    result = session.execute(statement).mappings().all()

    return {'data': result}

@router.post("/",
    response_model= MemberPublic,
    status_code=201,
    description=Path('app/openapi_docs/api/v1/post_members_MemberCreate.md').read_text(),
    dependencies=[Depends(security.access_token_required)]
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