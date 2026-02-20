from datetime import date

from pydantic import BaseModel

import models


#Author_data_model___________________________________________________________________
class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True


#Book_data_model_______________________________________________________________________

class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date

class BookCreate(BookBase):
    author_id: int


class Book(BookBase):
    id: int
    author: Author

    class Config:
        from_attributes = True
