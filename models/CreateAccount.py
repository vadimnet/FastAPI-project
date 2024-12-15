from pydantic import BaseModel


class CreateAccount(BaseModel):
    login: str
    password: str
    firstname: str
    lastname: str
    date_b: str|None #позже поменяю на встроенный тип date
    role: str #добавить валидацию, так как роль может быть либо user, либо admin