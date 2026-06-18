from fastapi import APIRouter, UploadFile, File
from app.core.dependencies import ingestion_service

router = APIRouter()

@router.post("/ingest", tags=["ingest"])
async def ingest(file: UploadFile = File(...)):
    print(f"Received: {file.filename}")
    file_path = f"data/raw/{file.filename}"

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    result = ingestion_service.ingest_pdf(file_path)
    print(result)
    print(type(result))

    return result