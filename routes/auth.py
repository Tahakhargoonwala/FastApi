from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from config.db import db
from auth.jwt_handler import create_access_token
from passlib.context import CryptContext

auth_router = APIRouter()

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserLogin(BaseModel):
    username: str
    password: str

class UserSignup(UserLogin):
    about: str

@auth_router.post("/signup")
async def signup(user: UserSignup):
    user_in_db = db.users.find_one({"username": user.username})
    if user_in_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    hashed_password = pwd_context.hash(user.password)
    db.users.insert_one({
        "username": user.username,
        "password": hashed_password,
        "about": user.about,
        "is_enable": True
    })

    return {"message": "User created successfully"}

@auth_router.post("/login")
async def login(user: UserLogin):
    user_in_db = db.users.find_one({"username": user.username})
    if not user_in_db or not pwd_context.verify(user.password, user_in_db["password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token({"sub": user_in_db["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
