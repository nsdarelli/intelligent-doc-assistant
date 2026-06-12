from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
from app.services.llm_service import LLMService

query = "What is the interest rates offered by various banks?"

embedding_service = EmbeddingService()
query_embedding = embedding_service.embed_query(query)

vector_service = VectorService()
context = vector_service.retrieve_context(query_embedding)
print(f"\nContext:\n{context}")

llm_service = LLMService()

answer = llm_service.generate_response(query=query, context=context)

print(f"\nAnswer:\n")
print(answer)