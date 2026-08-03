from fastapi import FastAPI
from app.api.routes.document_routes import router as document_router

app = FastAPI(
  title="DocuMind AI",
  version="1.0.0",
)

app.include_router(document_router)