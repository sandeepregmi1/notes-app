# /home/sandeep/Projects/notes_app/app/utils.py
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


# here password is the plain text password and 
# hashed_password is the hashed version stored in the database. 
# The function returns True if the password matches, otherwise False.