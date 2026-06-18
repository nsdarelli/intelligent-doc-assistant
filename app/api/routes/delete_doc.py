from app.core.dependencies import document_service

from fastapi import APIRouter

router = APIRouter()

@router.delete("/documents/{source}")
def delete_document(source: str):
    return document_service.delete_document(source)