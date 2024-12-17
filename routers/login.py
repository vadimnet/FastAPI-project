from fastapi import APIRouter, Query
from typing import Annotated

router = APIRouter(
    prefix="/api/v1.0/"
)

@router.put("login")
async def login():
    pass

@router.put("register")
async def register():
    pass

@router.put("logout")
async def logout():
    pass
