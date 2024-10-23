from fastapi import APIRouter

authRouter = APIRouter(prefix="/signup", tags=["auth"])


@authRouter.post("/")
async def create_user_account():
    pass
