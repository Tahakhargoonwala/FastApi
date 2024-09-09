# from fastapi import FastAPI
# from routes.user import user
# app = FastAPI()
# app.include_router(user) 


from fastapi import FastAPI
from routes.auth import auth_router
from routes.script import script_router

app = FastAPI()

# Include the routes
app.include_router(auth_router, prefix="/auth")
app.include_router(script_router, prefix="/script")
