# /home/sandeep/Projects/notes_app/app/routers/notes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db
from app.oauth2 import get_current_user

router = APIRouter(prefix="/notes", tags=["Notes"])


# CREATE NOTE
@router.post("/")
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    new_note = models.Note(
        title=note.title,
        content=note.content,
        owner_id=user_id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


# GET ALL NOTES (USER SPECIFIC + PAGINATION)
@router.get("/")
def get_notes(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user),
    limit: int = 10,
    skip: int = 0
):

    notes = db.query(models.Note)\
        .filter(models.Note.owner_id == user_id)\
        .limit(limit)\
        .offset(skip)\
        .all()

    return notes