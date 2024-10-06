from typing import Optional
from fastapi import FastAPI, Header
from pydantic import BaseModel

import src.books.data as db

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World!"}


@app.get("/greet")
async def greet(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Ola {name}", "age": f"age: {age}"}


class Book(BaseModel):
    title: str
    author: str


@app.post("/create_book")
async def create_book(book: Book):
    return {"title": book.title, "author": book.author}


@app.get("/get_headers")
async def get_header(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headers = {}

    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return request_headers
