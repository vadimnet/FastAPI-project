from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1.0/login"
)

@router.put("/api/v1.0/login")
async def login():
    pass
