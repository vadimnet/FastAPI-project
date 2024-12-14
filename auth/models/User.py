from pydantic import BaseModel

class User(BaseModel):
    token: str
    username: str
    password_hash: str