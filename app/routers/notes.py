# /home/sandeep/Projects/notes_app/app/routers/notes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db
from app.oauth2 import get_current_user

from app.crud import get_user_note 


from app.schemas import NoteUpdate

router = APIRouter(prefix="/notes", tags=["Notes"])


# CREATE NOTE
@router.post("/", response_model=schemas.NoteResponse)
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
@router.get("/", response_model=list[schemas.NoteResponse])
def get_notes(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user),
    limit: int = 10,
    skip: int = 0
):

    notes = db.query(models.Note)\
        .filter(models.Note.owner_id == user_id,
                models.Note.is_deleted == False
        )\
        .limit(limit)\
        .offset(skip)\
        .all()

    return notes

# GET NOTE BY ID
@router.get("/{note_id}", response_model=schemas.NoteResponse)
def get_note_by_id(
    note_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    note = get_user_note(db, note_id, user_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return note

# DELETE NOTE
@router.delete("/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    note = get_user_note(db, note_id, user_id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note.is_deleted = True
    db.commit()

    return {"message": "Note deleted (soft delete)"}



# UPDATE NOTE
@router.put("/{note_id}", response_model=schemas.NoteResponse)
def update_note(
    note_id: int,
    updated_note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    note = get_user_note(db, note_id, user_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note.title = updated_note.title
    note.content = updated_note.content
    db.commit()
    db.refresh(note)

    return note

@router.patch("/{note_id}", response_model=schemas.NoteResponse)
def patch_note(
    note_id: int,
    updated_note: schemas.NoteUpdate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.owner_id == user_id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    update_data = updated_note.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(note, key, value)

    db.commit()
    db.refresh(note)

    return note

@router.put("/restore/{note_id}")
def restore_note(
    note_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):

    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.owner_id == user_id
    ).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note.is_deleted = False
    db.commit()
    db.refresh(note)

    return {"message": "Note restored successfully"}