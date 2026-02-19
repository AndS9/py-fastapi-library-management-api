from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), nullable=False, unique=False)
    summary = Column(String(512), nullable=False)
    publication_date = Column(Date, nullable=True)
    author_id = Column(Integer, ForeignKey("authors.id"))


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False, unique=True)
    bio = Column(String(512), nullable=True)
    Books = relationship(Book)