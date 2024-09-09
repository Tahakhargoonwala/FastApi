from fastapi import APIRouter, Depends, HTTPException
from models.script import Script
from config.db import db
from schemas.script import scriptEntity, scriptsEntity
from auth.jwt_handler import verify_token

script_router = APIRouter()

@script_router.get("/")
async def get_all_scripts(token: str = Depends(verify_token)):
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    scripts = db.scripts.find({"is_enable": True})
    return scriptsEntity(scripts)

@script_router.post("/")
async def create_script(script: Script, token: str = Depends(verify_token)):
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    db.scripts.insert_one(dict(script))
    return {"message": "Script added successfully"}

@script_router.put("/assign/{script_id}")
async def assign_script_to_user(script_id: str, token: str = Depends(verify_token)):
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    db.users.update_one(
        {"username": token["sub"]},
        {"$addToSet": {"scripts": script_id}}
    )
    return {"message": "Script assigned to user"}

@script_router.get("/my-scripts")
async def get_user_scripts(token: str = Depends(verify_token)):
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.users.find_one({"username": token["sub"]})
    script_ids = user.get("scripts", [])
    scripts = db.scripts.find({"_id": {"$in": script_ids}, "is_enable": True})
    return scriptsEntity(scripts)
