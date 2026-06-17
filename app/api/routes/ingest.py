from fastapi import APIRouter, UploadFile, File
from app.core.dependencies import ingestion_service

router = APIRouter()

@router.post("/ingest", tags=["ingest"])
async def ingest(file: UploadFile = File(...)):
    file_path = f"data/raw/{file.filename}"

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    result = ingestion_service.ingest_pdf(file_path)

    return result