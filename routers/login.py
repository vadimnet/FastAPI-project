from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1.0/"
)

@router.put("login")
async def login():
    pass

@router.put("sign-up")
async def sign_up():
    pass


