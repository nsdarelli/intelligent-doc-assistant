from app.core.dependencies import document_service
from app.core.exceptions import DocNotFoundError

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.delete("/documents/{source}")
def delete_document(source: str):
    try:
        return document_service.delete_document(source)
    except DocNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"{str(e)}")