from fastapi import FastAPI
from src.books.routes import router as books_router

app = FastAPI()

app.include_router(books_router)
