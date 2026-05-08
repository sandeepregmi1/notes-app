# /home/sandeep/Projects/notes_app/app/dependencies.py
from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# This file contains the dependency for getting a database session. 
# It uses the SessionLocal class from the database module 
# to create a new session and ensures that it is properly closed after use.
# The get_db function can be used as a dependency in FastAPI routes to provide access 
# to the database session.

# return is not used here because we want to ensure
#  that the database session is closed after the route handler is done using it.

# yield is used to create a generator that can be used in FastAPI's dependency injection system.
# When a route depends on get_db, FastAPI will call the function and yield the database 
# session to the route handler.
#