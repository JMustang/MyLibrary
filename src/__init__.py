from fastapi import FastAPI
from src.books.routes import router as books_router


version = "v1"

app = FastAPI(
    version=version,
    title="My Library",
    description="A REST API for a book review web service",
)

app.include_router(books_router, prefix=f"/api/{version}/books", tags=["books"])
