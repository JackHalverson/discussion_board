from fastapi import FastAPI, HTTPException, Depends, status
from sqlmodel import Session, select
from sqlalchemy.orm import Session
import models
from typing import Annotated
from database import engine, SessionLocal
from models import User, Group, Topic, Comment
import auth
from auth import get_current_user


app = FastAPI()
app.include_router(auth.router)

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


#User functions
@app.post("/users/")
async def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
@app.get("/")
async def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"User": user}

#Group functions
@app.post("/groups/")
async def create_group(group: Group):
    with Session(engine) as session:
        session.add(group)
        session.commit()
        session.refresh(group)
        return group
    
@app.get("/groups/")
async def read_groups():
    with Session(engine) as session:
        groups = session.execute(select(Group)).all()
        return groups
    
@app.delete("/groups/{group_id}")
async def delete_group(group_id: int):
    with Session(engine) as session:
        group = session.get(Group, group_id)
        if group is None:
            raise HTTPException(status_code=404, detail="Group not found")
        session.delete(group)
        session.commit()
        return {"message": "Group deleted successfully"}
    

#Topic functions
@app.post("/topics/")
async def create_topic(topic: Topic):
    with Session(engine) as session:
        session.add(topic)
        session.commit()
        session.refresh(topic)
        return topic
    
@app.get("/topics/{group_id}/")
async def read_topics(group_id: int):
    with Session(engine) as session:
        topics = session.execute(select(Topic).where(Topic.group_id == group_id)).all()
        return topics
    
@app.delete("/topics/{topic_id}")
async def delete_topic(topic_id: int):
    with Session(engine) as session:
        topic = session.get(Topic, topic_id)
        if topic is None:
            raise HTTPException(status_code=404, detail="Topic not found")
        session.delete(topic)
        session.commit()
        return {"message": "Topic deleted successfully"}


#Comments functions
@app.post("/comments/")
async def create_comment(comment: Comment):
    with Session(engine) as session:
        session.add(comment)
        session.commit()
        session.refresh(comment)
        return comment
    
@app.get("/comments/{topic_id}/")
async def read_comments(topic_id: int):
    with Session(engine) as session:
        comments = session.execute(select(Comment).where(Comment.topic_id == topic_id)).all()
        return comments
    
@app.delete("/comments/{comment_id}")
async def delete_comment(comment_id: int):
    with Session(engine) as session:
        comment = session.get(Comment, comment_id)
        if comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")
        session.delete(comment)
        session.commit()
        return {"message": "Comment deleted successfully"}