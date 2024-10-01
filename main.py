from fastapi import FastAPI

import data as db

app = FastAPI()


@app.get("/books")
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
