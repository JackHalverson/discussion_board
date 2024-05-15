from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from database import engine
from models import Topic


router = APIRouter(
    prefix="/topics",
    tags=["topics"]
)

@router.post("/")
async def create_topic(topic: Topic):
    with Session(engine) as session:
        session.add(topic)
        session.commit()
        session.refresh(topic)
        return topic
    
@router.get("/{group_id}/")
async def read_topics(group_id: int):
    with Session(engine) as session:
        topics = session.exec(select(Topic).where(Topic.group_id == group_id)).all()
        return topics
    
@router.get("/{user_id}/")
async def read_user_topics(user_id: int):
    with Session(engine) as session:
        topics = session.exec(select(Topic).where(Topic.owner_id == user_id)).all()
        return topics

@router.delete("/{topic_id}")
async def delete_topic(topic_id: int):
    with Session(engine) as session:
        topic = session.get(Topic, topic_id)
        if topic is None:
            raise HTTPException(status_code=404, detail="Topic not found")
        session.delete(topic)
        session.commit()
        return {"message": "Topic deleted successfully"}