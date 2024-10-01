from fastapi import FastAPI
from pydantic import BaseModel

import data as db

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


@app.get("/books", response_model=list[Book])
async def get_books():
    return db.books


@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    return db.books[book_id]


@app.post("/books")
async def create_books() -> dict:
    db.books.append(book)


@app.patch("/book/{book_id}")
async def update_book(book_id: int) -> dict:
    return db.books[book_id]


@app.delete("/book/{book_id}")
async def delete_book(book_id: int) -> dict:
    return db.books[book_id]
