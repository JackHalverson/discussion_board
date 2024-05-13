from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from models import User, Group, Topic, Comment, engine

from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request


app = FastAPI()


#User functions
@app.post("/users/")
async def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        session.delete(user)
        session.commit()
        return {"message": "User deleted successfully"}
    

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
        groups = session.exec(select(Group)).all()
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
        topics = session.exec(select(Topic).where(Topic.group_id == group_id)).all()
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
        comments = session.exec(select(Comment).where(Comment.topic_id == topic_id)).all()
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