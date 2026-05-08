# /home/sandeep/Projects/notes_app/app/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    notes = relationship("Note", back_populates="owner")


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="notes")

    is_deleted = Column(Boolean, default=False, nullable=False)  # Soft delete flag