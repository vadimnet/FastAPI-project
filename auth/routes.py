from fastapi import APIRouter
from models import User

router = APIRouter()

@router.put(/api/v1/auth/login)
async def login(user: User):
    pass
