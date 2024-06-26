from sqlmodel import Field, SQLModel, create_engine
from datetime import datetime
from database import Base

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str
    name: str
    disabled: bool = False
    hashed_password: str
    
class Group(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    date_posted: datetime
    owner_id: int = Field(foreign_key="user.id")

class Topic(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    description: str | None = None
    date_posted: datetime
    group_id: int = Field(foreign_key="group.id")
    owner_id: int = Field(foreign_key="user.id")

class Comment(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    content: str
    date_posted: datetime
    topic_id: int = Field(foreign_key="topic.id")
    owner_id: int = Field(foreign_key="user.id")
