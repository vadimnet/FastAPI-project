from fastapi import APIRouter, Query, Body, Path
from typing import Annotated
from models import AdminCreateAccountDTO
from models.UpdateAccountDTO import UpdateAccountDTO
from models.AdminUpdateAccountDTO import AdminUpdateAccountDTO

router = APIRouter(
    prefix="/api/v1.0/"
)

@router.get("accounts")
async def accounts():
    pass

@router.put("accounts")
async def delete_account(id: Annotated[int, Query(gt=0)]):
    pass

@router.post("accounts")
async def create_account(account: Annotated[AdminCreateAccountDTO, Body()]): #попробовать сделать через Annotated
    pass

@router.put("accounts/{id}")
async def change_account(id: int, account: Annotated[UpdateAccountDTO|AdminUpdateAccountDTO, Body()]):
    pass

@router.get("account/{id}")
async def get_account(id: Annotated[int, Path()]):
    pass

@router.put("account")
async def change_account(account: Annotated[UpdateAccountDTO|AdminUpdateAccountDTO, Body()]):
    pass
