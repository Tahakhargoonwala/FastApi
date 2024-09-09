# from fastapi import APIRouter
# from models.user import User
# from config.db import conn
# from bson.objectid import ObjectId

# from schemas.user import userEntity,usersEntity

# user = APIRouter()

# @user.get("/")
# async def find_all_users():
#     print(usersEntity(conn.local.users.find()))
#     return usersEntity(conn.local.users.find())

# @user.get("/{id}")
# async def find_user(id):
#     return userEntity(conn.local.users.find_one({"_id":ObjectId(id)}))
    

# @user.post("/")
# async def create_user(user:User):
#     conn.local.users.insert_one(dict(user))
#     return userEntity(conn.local.users.find())


# @user.put("/{id}")
# async def update_user(id,user:User):
#     conn.local.users.update_one({"_id":ObjectId(id)},{"$set":dict(user)})
#     return userEntity(conn.local.users.find_one({"_id":ObjectId(id)}))

# @user.delete("/{id}")
# async def delete_user(id,user:User):
#     return userEntity(conn.local.users.find_one_and_delete({"_id":ObjectId(id)}))

  