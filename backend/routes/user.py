from fastapi import APIRouter, HTTPException
from sqlmodel import Session
from fastapi import Depends
from typing import Annotated
from database import SessionLocal
from routes.auth import get_current_user , get_user_id


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
id_dependency = Annotated[int, Depends(get_user_id)]


@router.get("/")
async def user_info(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"User": user}

@router.get("/id/")
def user_id(user_id: id_dependency):
    if user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_id