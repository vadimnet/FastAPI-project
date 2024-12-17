from fastapi import APIRouter, Query, Body
from typing import Annotated
from models import CreateAccount

router = APIRouter(
    prefix="/api/v1.0/"
)

@router.get("accounts")
async def accounts():
    pass

@router.put("accounts")
async def delete_account(id: Annotated[int, Query(gt=0)]):
    pass

@router.put("accounts")
async def create_account(account: CreateAccount): #попробовать сделать через Annotated
    pass

@router.put("accounts/{id}")
async def change_account(id: int, account:CreateAccount): #сделать отдельную pydantic модель?(или просто сделать текущую универсальной)
    pass

@router.get("account")
async def account(id: Annotated[int, Query()]):
    pass

@router.put("account")
async def change_account(account: Annotated[CreateAccount, Body()]):
    pass
