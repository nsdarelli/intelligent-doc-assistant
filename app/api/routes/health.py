from fastapi import APIRouter

router = APIRouter(tags=["Health"])

@router.get("/health", summary="Health Check", description="Check the health of the application.")
def health_check():
    return {"status": "healthy"}