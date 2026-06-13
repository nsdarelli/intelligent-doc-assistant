from google import genai
from app.core.config import settings
import time
from google.genai.errors import ServerError

class LLMService:

    def __init__(self):

        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model = settings.MODEL_NAME

    def generate_response(self, query: str, context: str):
        prompt = f"""
        You are a helpful document assistant.

        Use ONLY the supplied context.

        If the answer cannot be found in the context,
        respond with:

        "I could not find that information in the document."

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

        max_retries = 3

        for attempt in range(max_retries):
            try:
                response = self.client.models.generate_content(
                    model = self.model,
                    contents = prompt
                )

                return response.text
            
            except ServerError as e:
                if attempt == max_retries - 1:
                    raise
                
                wait_time = 2**attempt # Exponential backoff
                print(f"Server error: {e}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)