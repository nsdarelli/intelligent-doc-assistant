from google import genai
from app.core.config import settings

class LLMService:

    def __init__(self):

        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = settings.MODEL_NAME

    def generate_response(self, query: str, context: str):
        prompt = """
        You are a helpful document assistant.
        Answer ONLY using the provided context.

        Context:
        {context}

        Question:
        {query}
        """

        response = self.client.models.generate_content(
            model = self.model,
            contents = prompt
        )

        return response.text    