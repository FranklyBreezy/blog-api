from sqlalchemy.orm import DeclarativeBase , relationship
from uuid import uuid4
from sqlalchemy import Column , String , DateTime , ForeignKey
from datetime import datetime
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id = Column(
        String,
        default=lambda : str(uuid4),
        primary_key=True
    )

    username = Column(
        String,
        unique=True,
        nullable= False
    )

    password_hash = Column(
        String,
        nullable = False
    )

    created_at = Column(
        DateTime,
        default = datetime.utcnow,
        nullable = False
    )

    updated_at= Column(
        DateTime,
        default = datetime.utcnow,
        onupdate = datetime.utcnow,
        nullable = False
    )

    article = relationship("Article")
    blog = relationship("Blog")

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(
        String,
        default = lambda :  str(uuid4),
        primary_key = True
    )

    title = Column(
        String,
        unique = True,
        nullable = False
    )

    user_id = Column(
        String,
        ForeignKey(User.id),
        nullable = False
    )

    created_at = Column(
        DateTime,
        default = datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default = datetime.utcnow,
        onupdate = datetime.utcnow
    )

class Article(Base):
    __tablename__ = "articles"

    id = Column(
        String,
        default = lambda : str(uuid4),
        primary_key = True
    )

    title = Column(
        String,
        nullable = False
    )

    blog_id = Column(
        String,
        ForeignKey(Blog.id),
        nullable = False
    )

    content = Column(
        String,
    )

