from datetime import date

from pydantic import BaseModel


#Author_data_model___________________________________________________________________
class AuthorBase(BaseModel):
    name: str
    bio: str | None


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        model_config = {"from_attributes": True}


#Book_data_model_______________________________________________________________________

class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: date | None

class BookCreate(BookBase):
    author_id: int


class Book(BookBase):
    id: int
    author: Author

    class Config:
        model_config = {"from_attributes": True}
