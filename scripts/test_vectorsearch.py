from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService

query = "What is this document about?"

embedding_service = EmbeddingService()
query_embedding = embedding_service.embed_query(query)

vector_service = VectorService()
results = vector_service.search(query_embedding)

print(f"Results: {results['documents']}")  # Print the retrieved documents based on the query