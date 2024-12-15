from fastapi import FastAPI
from routers import login, accounts

app = FastAPI()

app.include_router(login.router)
app.include_router(accounts.router)

