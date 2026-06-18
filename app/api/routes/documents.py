from fastapi import APIRouter
from app.core.dependencies import document_service

router = APIRouter()

@router.get("/documents")
def get_documents():
    return document_service.list_documents()

