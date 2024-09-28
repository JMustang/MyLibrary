from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World!"}


@app.get("/greet")
async def greet(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Ola {name}", "age": f"age: {age}"}


@app.post("/create_book")
async def create_book():
    pass
