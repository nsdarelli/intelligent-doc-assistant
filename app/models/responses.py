from pydantic import BaseModel

class Sources(BaseModel):
    source: str
    page_number: int
    chunk_id: int 

class ChatResponse(BaseModel):
    response: str
    sources: list[Sources]