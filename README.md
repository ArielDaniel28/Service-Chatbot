# Service Chatbot Based on OpenAI API
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

# Documentation for Running and Testing the Chatbot Agent
## Setting Up the Environment and Dependencies
Install Python: Ensure Python 3.7 or later is installed on your machine. You can download it from python.org.

Install Dependencies: Open command line interface and run the following command to install all necessary libraries:

**pip install openai python-dotenv sqlite3**

## Running the Chatbot
### Run the Code Using Python:

Open the command line interface.
Navigate to the directory where your code files are located.
Run the following command:

**python Conversation.py**

### Run the Code Using the Executable:

Locate the Conversation.exe file in your file explorer.
Double-click the Conversation.exe file to start the chatbot.
The chatbot will start a conversation with you. You can ask questions related to company policies, order status, etc.

## Testing the Chatbot
Example Database: An example database file named orders.db is provided with the project. This file includes a sample orders table with columns order_number and status.

Additional Tests: Try asking the chatbot questions like "What is the status of my order?" or request to speak with a human representative to ensure the respective functions work correctly.
