from pydantic import BaseModel, Field


class UserCreateModel(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=3, max_length=50)
