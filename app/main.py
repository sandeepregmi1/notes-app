# /home/sandeep/Projects/notes_app/app/main.py
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, notes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(notes.router)


@app.get("/")
def root():
    return {"message": "Notes API Ready 🚀"}