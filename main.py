from fastapi import FastAPI, status
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


# GET
@app.get("/books", response_model=list[Book])
async def get_books():
    return db.books


# GET BY ID
@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    return db.books[book_id]


# POST
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_books(book_data: int) -> dict:
    new_book = book_data.model_dump()

    db.books.append(new_book)

    return new_book


# UPDATE
@app.patch("/book/{book_id}")
async def update_book(book_id: int) -> dict:
    return db.books[book_id]


# DELETE
@app.delete("/book/{book_id}")
async def delete_book(book_id: int) -> dict:
    return db.books[book_id]
