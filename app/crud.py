from sqlalchemy.orm import Session
from app import models

def get_user_note(db: Session, note_id: int, user_id: int):
    return db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.owner_id == user_id
    ).first()