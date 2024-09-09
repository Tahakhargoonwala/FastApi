# from pydantic import BaseModel
# class User(BaseModel): 
#     name: str
#     email: str
#     password: str

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    is_enable: bool = True
    about: str = ""
