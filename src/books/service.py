from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import CreateBookModel, UpdateBookModel
from sqlmodel import select, desc
from .models import Book


class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))

        result = await session.exec(statement)
        return result.all()

    async def get_book_by_id(self, book_uid: str, session: AsyncSession):
        statement = select(Book).where(Book.uid == book_uid)

        result = await session.exec(statement)
        book = result.first()
        return book if book is not None else None

    async def create_book(self, book_data: CreateBookModel, session: AsyncSession):
        pass

    async def update_book(
        self, book_uid: str, update_date: UpdateBookModel, session: AsyncSession
    ):
        pass

    async def delete_book(self, book_uid: str, session: AsyncSession):
        pass
