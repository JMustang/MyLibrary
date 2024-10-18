from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from src.books.schemas import Book, UpdateBookModel
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.books.models import Book
from src.db.main import get_session

router = APIRouter()
book_service = BookService()


# GET
@router.get("/", response_model=list[Book])
async def get_books(session: AsyncSession = Depends(get_session)):
    db = await book_service.get_all_books(session)
    return db


# GET BY ID
@router.get("/{book_uid}")
async def get_book(book_uid: int, session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_book_by_id(book_uid, session)

    if book:
        return
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )


# POST
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_books(
    book_data: Book, session: AsyncSession = Depends(get_session)
) -> dict:
    new_book = await book_service.create_book(book_data, session)

    return new_book


# UPDATE
@router.patch("/{book_uid}")
async def update_book(
    book_uid: int,
    updateBook: UpdateBookModel,
    session: AsyncSession = Depends(get_session),
) -> dict:
    update_book = await book_service.update_book(book_uid, updateBook, session)

    if update_book:
        return update_book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )


# DELETE
@router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(
    book_uid: int, session: AsyncSession = Depends(get_session)
):
    book = await book_service.delete_book(book_uid, session)

    if book:
        return None
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
