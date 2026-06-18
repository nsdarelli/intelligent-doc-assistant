from fastapi import APIRouter

from app.models.requests import ChatRequest
from app.models.responses import ChatResponse
from app.core.dependencies import embedding_service, vector_service, llm_service


router = APIRouter(tags=["Chat"])

@router.post("/chat", response_model=ChatResponse, summary="Chat with the assistant", description="Send a query to the assistant and receive a response.")
def chat(request: ChatRequest):
    try:
        query_embedding = embedding_service.embed_query(request.query)
        retrieval_result = vector_service.retrieve_context(query_embedding)
        response = llm_service.generate_response(query=request.query, context=retrieval_result["documents"])

        return ChatResponse(response=response, sources=retrieval_result["sources"])
    except Exception as e:
        print(f"Error in chat: {str(e)}")
        return ChatResponse(response=f"Error: {str(e)}", sources=[])
