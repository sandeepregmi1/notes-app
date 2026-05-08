# /home/sandeep/Projects/notes_app/app/schemas.py
from pydantic import BaseModel


# USER
class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str
    


# NOTE
class NoteCreate(BaseModel):
    title: str
    content: str