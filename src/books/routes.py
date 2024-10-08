from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.books.schemas import Book, UpdateBookModel

from src.books.data import books as db

router = APIRouter(prefix="/books", tags=["books"])


# GET
@router.get("/", response_model=list[Book])
async def get_books():
    return db


# GET BY ID
@router.get("/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in db:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# POST
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_books(book_data: Book) -> dict:
    new_book = book_data.model_dump()

    db.append(new_book)

    return new_book


# UPDATE
@router.patch("/{book_id}")
async def update_book(book_id: int, updateBook: UpdateBookModel) -> dict:
    for book in db:
        if book["id"] == book_id:
            book.update(updateBook.model_dump())
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# DELETE
@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in db:
        if book["id"] == book_id:
            db.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
