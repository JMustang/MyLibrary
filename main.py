from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
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


class UpdateBookModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


# GET
@app.get("/books", response_model=list[Book])
async def get_books():
    return db.books


# GET BY ID
@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in db.books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# POST
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_books(book_data: Book) -> dict:
    new_book = book_data.model_dump()

    db.books.append(new_book)

    return new_book


# UPDATE
@app.patch("/book/{book_id}")
async def update_book(book_id: int, updateBook: UpdateBookModel) -> dict:
    for book in db.books:
        if book["id"] == book_id:
            book.update(updateBook.model_dump())
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# DELETE
@app.delete("/book/{book_id}")
async def delete_book(book_id: int) -> dict:
    return db.books[book_id]
