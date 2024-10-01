from fastapi import FastAPI

import data as db

app = FastAPI()


@app.get("/books")
async def get_books():
    return db.books


@app.post("/books")
async def create_books():
    db.books.append(book)
