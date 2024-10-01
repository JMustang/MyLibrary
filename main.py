from fastapi import FastAPI

import data as db

app = FastAPI()


@app.get("/books")
async def get_books():
    return db.books


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return db.books[book_id]


@app.post("/books")
async def create_books():
    db.books.append(book)
