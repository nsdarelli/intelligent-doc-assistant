from fastapi import APIRouter, HTTPException
import time

from app.models.requests import ChatRequest
from app.models.responses import ChatResponse
from app.core.dependencies import embedding_service, vector_service, llm_service
from app.core.logger import logger
from app.core.exceptions import RetrievalException


router = APIRouter(tags=["Chat"])

@router.post("/chat", response_model=ChatResponse, summary="Chat with the assistant", description="Send a query to the assistant and receive a response.")
def chat(request: ChatRequest):
    try:
        start = time.time()
        logger.info(f"Question received: {request.query}")
        query_embedding = embedding_service.embed_query(request.query)
        retrieval_result = vector_service.retrieve_context(query_embedding)
        response = llm_service.generate_response(query=request.query, context=retrieval_result["documents"])
        logger.info(f"Response Generated Successfully")
        duration = time.time() - start
        logger.info(f"Query completed in {duration:.2f} seconds")

        return ChatResponse(response=response, sources=retrieval_result["sources"])
    except RetrievalException as e:
        raise HTTPException(status_code=500, detail=str(e))
        # print(f"Error in chat: {str(e)}")
        # return ChatResponse(response=f"Error: {str(e)}", sources=[])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected Error: {str(e)}")
