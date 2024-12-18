from fastapi import APIRouter, Query
from typing import Annotated

router = APIRouter(
    prefix="/api/v1.0/"
)

@router.post("login")
async def login():
    pass

@router.post("register")
async def register():
    pass

@router.post("logout")
async def logout():
    pass
