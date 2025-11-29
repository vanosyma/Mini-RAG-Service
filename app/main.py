from fastapi import FastAPI
from .api.routes import router

app = FastAPI(title="Refactored RAG Service")
app.include_router(router)