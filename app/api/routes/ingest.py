from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.dependencies import ingestion_service
from app.core.logger import logger
from app.core.exceptions import DocumentProcessingException, DuplicateDocumentException, UnsupportedFileTypeException

router = APIRouter()

@router.post("/ingest", tags=["ingest"])
async def ingest(file: UploadFile = File(...)):
    print(f"Received: {file.filename}")
    try:
        file_path = f"data/raw/{file.filename}"

        contents = await file.read()

        with open(file_path, "wb") as f:
            f.write(contents)

        result = ingestion_service.ingest_document(file_path)
        logger.info(f"Ingestion completed for {file.filename}")
        print(result)
        print(type(result))

        return result
    
    except DuplicateDocumentException as e:
        raise HTTPException(
            status_code=409, detail=str(e)
        )
    except UnsupportedFileTypeException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except DocumentProcessingException as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")