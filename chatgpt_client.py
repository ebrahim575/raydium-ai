from openai import OpenAI
from creds import openaiapikey

class ChatGPTClient:
    def __init__(self):
        self.client = OpenAI(api_key=openaiapikey)
        self.persona_prompt = """
                    You are an intelligent cryptocurrency advisor, you give opinions and process commands.
                    However in this instance you are being used as a mock implementation of processing, so you will pretend you executed an action but in reality you did not. 
                    Such as \"please change $10k of BTC into XRP\" And you will not mention that you are in demo mode you will pretend you actually did it.
                    You also provide extra information as what you processed coins into, why you did it, and some extra information about the latest information about the coins such as trends and price.

                """

    def get_response(self, input_text: str) -> str:
        """Takes input text and returns ChatGPT's response using the persona."""
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.persona_prompt},
                    {"role": "user", "content": input_text}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"