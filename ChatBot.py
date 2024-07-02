from openai import OpenAI


class ChatBot:
    def __init__(self, key):
        self.client = OpenAI(api_key=key)
        self.model = "gpt-3.5-turbo"
        self.temperature = 0.5

    def get_response(self, chat_history):
        response = self.client.chat.completions.create(
            model=self.model, messages=chat_history, temperature=self.temperature,
        )
        return response.choices[0].message.content
