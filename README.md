## Service Chatbot Based on OpenAI API
## Overview
Developed the "Service Chatbot Based on OpenAI API" using Python and OpenAI API. This project leverages object-oriented programming (OOP) principles to design a modular architecture. The chatbot is capable of handling customer inquiries related to order status, return policies, and more.

## Features
Order Status Management: Integrated with SQLite to track and retrieve the status of customer orders.
User Information Storage: Utilizes CSV to store user contact information securely.
Secure API Key Management: Ensures security with environment variables (.env) for managing API keys.
Natural Language Processing: Uses OpenAI API to understand and respond to customer inquiries effectively.
Modular Architecture: Designed using OOP principles to maintain clean, readable, and maintainable code.

## How It Works
ChatBot Class: Initializes the OpenAI API and manages the chat history.
Company Class: Contains the company's policies and provides a method to get the policies as text.
Conversation.py: Manages the flow of the conversation, checking for keywords to determine if the user wants to speak with a human representative or check order status.
Database Integration: Connects to an SQLite database to retrieve order status based on the order number provided by the user.
User Information Storage: Collects and saves user contact details in a CSV file when a human representative is requested.