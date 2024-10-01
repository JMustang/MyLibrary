from fastapi import FastAPI

import data as db

app = FastAPI()


@app.get("/books")
async def get_books():
    return db.books
