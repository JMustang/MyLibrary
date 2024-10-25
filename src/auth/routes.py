from fastapi import APIRouter
from .schemas import UserCreateModel

authRouter = APIRouter(prefix="/signup", tags=["auth"])


@authRouter.post("/")
async def create_user_account(user_date: UserCreateModel):
    pass
