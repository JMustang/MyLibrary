from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from schemas import Book, UpdateBookModel

from data import books as db

app = FastAPI()


# GET
@app.get("/books", response_model=list[Book])
async def get_books():
    return db


# GET BY ID
@app.get("/books/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# POST
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_books(book_data: Book) -> dict:
    new_book = book_data.model_dump()

    db.append(new_book)

    return new_book


# UPDATE
@app.patch("/books/{book_id}")
async def update_book(book_id: int, updateBook: UpdateBookModel) -> dict:
    for book in db:
        if book["id"] == book_id:
            book.update(updateBook.model_dump())
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# DELETE
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in db:
        if book["id"] == book_id:
            db.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
