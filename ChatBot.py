from openai import OpenAI


class ChatBot:
    """
    A class to interact with the OpenAI API to generate conversational responses.

    Attributes:
    client (OpenAI): An instance of the OpenAI client initialized with the provided API key.
    model (str): The model used for generating responses, set to "gpt-3.5-turbo".
    temperature (float): The temperature setting for the model, which controls the randomness of the responses.
    """

    def __init__(self, key):
        """
        Initializes the ChatBot instance with the provided OpenAI API key.

        Parameters:
        key (str): The OpenAI API key used to authenticate requests.
        """
        self.client = OpenAI(api_key=key)
        self.model = "gpt-3.5-turbo"
        self.temperature = 0.5

    def get_response(self, chat_history):
        """
        Generates a response from the chatbot based on the provided chat history.

        Parameters:
        chat_history (list): A list of dictionaries representing the chat history. Each dictionary should have a
         'role' and 'content'.

        Returns:
        str: The chatbot's response.
        """
        response = self.client.chat.completions.create(
            model=self.model, messages=chat_history, temperature=self.temperature,
        )
        return response.choices[0].message.content
