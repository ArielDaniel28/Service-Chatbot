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
