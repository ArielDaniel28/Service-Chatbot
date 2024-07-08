# ChatBot UI Documentation
## Introduction
This documentation provides detailed instructions on how to set up, run, and test the ChatBot UI.

## Prerequisites
Before running the ChatBot UI, ensure you have the following prerequisites installed on your system:

Python 3.x
pip (Python package installer)

## Create and activate a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install the required dependencies:
pip install -r requirements.txt
Environment Setup
Set up the .env file:
Create a file named .env in the root directory of your project and add your OpenAI API key:

makefile
Copy code
OPENAI_API_KEY=your_openai_api_key
Create the SQLite database:
If you haven't already, create the orders.db database and populate it with the required tables. Here's an example of how to create the database:

python
Copy code
import sqlite3

conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE orders (
    order_number TEXT PRIMARY KEY,
    status TEXT NOT NULL
)
''')

# Example data
cursor.execute('''
INSERT INTO orders (order_number, status) VALUES
('12345', 'Shipped'),
('67890', 'Processing')
''')

conn.commit()
conn.close()
Running the ChatBot UI
Run the ChatBot UI:

bash
Copy code
python chatbot_ui.py
Interacting with the ChatBot:

A graphical window will open.
Type your messages in the input field and press Enter or click the "Send" button to interact with the ChatBot.
The ChatBot will respond to your messages and display them in the chat window.
Testing the ChatBot
To test the ChatBot, follow these steps:

Human Representative Request:

Type a message that includes keywords such as "human", "talk to a human", "human support", etc.
The ChatBot should respond by asking if you want to talk to a human representative.
Provide the necessary information (full name, email, phone number) as requested by the ChatBot.
Order Status Request:

Type a message that includes keywords such as "order status", "track my order", "order update", etc.
The ChatBot should respond by asking for your order ID.
Provide an order ID that exists in the database (e.g., "12345").
The ChatBot should respond with the status of the order.
General Conversation:

Type any general query related to the company, its products, services, or policies.
The ChatBot should respond appropriately based on the predefined logic.
Troubleshooting
No response from the ChatBot: Ensure your OpenAI API key is correctly set up in the .env file and that you have an active internet connection.
Database issues: Ensure the orders.db database is correctly set up and contains the necessary tables and data.
Conclusion
This documentation provides all the necessary steps to set up, run, and test the ChatBot UI. If you encounter any issues or have further questions, please refer to the troubleshooting section or contact the project maintainers.

