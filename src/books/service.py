from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import CreateBookModel


class BookService:
    async def get_all_books(self, session: AsyncSession):
        pass

    async def get_book_by_id(self, book_uid: str, session: AsyncSession):
        pass

    async def create_book(self, book_data: CreateBookModel, session: AsyncSession):
        pass
