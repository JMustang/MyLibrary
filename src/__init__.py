from fastapi import FastAPI
from src.books.routes import router as books_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server starting up...")
    await init_db()
    yield
    print("Server shutting down...")


version = "v1"

app = FastAPI(
    version=version,
    title="My Library",
    description="A REST API for a book review web service",
    lifespan=life_span,
)

app.include_router(books_router, prefix=f"/api/{version}/books", tags=["books"])
