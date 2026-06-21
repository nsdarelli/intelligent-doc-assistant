from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.health import router as health_router
from app.api.routes.chat import router as chat_router
from app.api.routes.ingest import router as ingest_router
from app.api.routes.documents import router as document_router
from app.api.routes.delete_doc import router as document_delete_router

app = FastAPI(title="Intelligent Document Assistant", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.include_router(health_router)
app.include_router(chat_router)
app.include_router(ingest_router)
app.include_router(document_router)
app.include_router(document_delete_router)
