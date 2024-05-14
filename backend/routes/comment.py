from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from database import engine
from models import Comment


router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@router.post("/")
async def create_comment(comment: Comment):
    with Session(engine) as session:
        session.add(comment)
        session.commit()
        session.refresh(comment)
        return comment
    
@router.get("/{topic_id}/")
async def read_comments(topic_id: int):
    with Session(engine) as session:
        comments = session.execute(select(Comment).where(Comment.topic_id == topic_id)).all()
        return comments
    
@router.delete("/{comment_id}")
async def delete_comment(comment_id: int):
    with Session(engine) as session:
        comment = session.get(Comment, comment_id)
        if comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")
        session.delete(comment)
        session.commit()
        return {"message": "Comment deleted successfully"}