from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from database import engine
from models import Group

router = APIRouter(
    prefix="/groups",
    tags=["groups"]
)

@router.post("/")
async def create_group(group: Group):
    with Session(engine) as session:
        session.add(group)
        session.commit()
        session.refresh(group)
        return group
    
@router.get("/")
async def read_groups():
    with Session(engine) as session:
        groups = session.exec(select(Group)).all()
        return groups
    
@router.get("/{user_id}/")
async def read_user_groups(user_id: int):
    with Session(engine) as session:
        groups = session.exec(select(Group).where(Group.owner_id == user_id)).all()
        return groups
    
@router.delete("/{group_id}")
async def delete_group(group_id: int):
    with Session(engine) as session:
        group = session.get(Group, group_id)
        if group is None:
            raise HTTPException(status_code=404, detail="Group not found")
        session.delete(group)
        session.commit()
        return {"message": "Group deleted successfully"}
    
