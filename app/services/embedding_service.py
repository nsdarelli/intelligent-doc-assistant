from google import genai
from app.core.config import settings
from google.genai import types
from app.core.logger import logger

class EmbeddingService:
    def __init__(self):
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = settings.EMBED_MODEL

    def embed_documents(self, texts):
        if not texts:
            return []
        
        embeddings = []
        batch_size = 25

        for i in range(0, len(texts), batch_size):
            batch = texts[i: i+batch_size]
            try:
                response = self.client.models.embed_content(model=self.model, contents=batch, config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT"))
                batch_embeddings = [emb.values for emb in response.embeddings]
                embeddings.extend(batch_embeddings)

            except Exception as e:
                logger.error(f"Error embedding batch {i // batch_size + 1}: {str(e)}")
                raise

        return embeddings
    
    def embed_query(self, query):
        try:
            response = self.client.models.embed_content(model=self.model, contents=query, config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY"))
            embeddings_q = response.embeddings[0].values
            logger.info(f"Embedding Dim: {len(embeddings_q)}")

            return embeddings_q
        except Exception as e:
            logger.error(f"Failed to generate query embedding: {str(e)}")
            raise