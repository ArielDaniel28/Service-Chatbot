from ChatBot import *
from Company import *
import csv
import sqlite3
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Initialize the company instance to access company policies
company = Company()

# Initialize chat history with system message containing the company policies and instructions for the chatbot
chat_history = [
    {
        "role": "system",
        "content": f""" You are a customer service chatbot for the company. You should 
only answer questions related to the company, its products, services, order status, return policies, and customer 
support. If you receive a question unrelated to the company, politely inform the user that you can only answer 
company-related questions. Company Policies: {company.get_policies_text()}. 
Note that you have been linked to a database includes orders ids and its status, if a costumer asks you about its
order status you can assume that we handle it via reliable way. If the customer asks you about the reliability of the
 information, you can respond that the information is reliable based on what is available
  in the company's systems.
  If the customer asks to know the status of their order or to speak with a human representative, ask them 
  to state it explicitly. Important: Under no circumstances should you ask the user for their order ID/number!!!
   In any such situation, ask them to explicitly state that they want to check the status of their order. in this case,
    ask the customer to write again in explicit way that he like to check the status of their order.""",
    }
]

# Keywords for detecting a request to speak with a human representative
hum_rep_keywords = [
    "human",
    "human being",
    "human representative",
    "talk to a human",
    "human support",
    "speak with a person",
    "real person",
    "live agent",
    "human agent",
    "customer service representative",
    "human assistance",
    "live support",
]

# Keywords for detecting user confirmation
verification_ans_keywords = [
    "yes",
    "yeah",
    "yup",
    "sure",
    "of course",
    "definitely",
    "absolutely",
    "please",
    "i do",
    "i would",
    "that's true",
    "true",
    "thats true",
    "confirm",
]

# Keywords for detecting a request to check order status
order_status_keywords = [
    "order status",
    "track my order",
    "order tracking",
    "check my order",
    "order progress",
    "order update",
    "status of my order",
    "where is my order",
    "order shipment",
    "order delivery",
    "order info",
    "order information",
    "order details",
    "order number",
    "delivery status",
    "status of my order",
    "status of order",
    "status of the order",
    "order to check",
]


def asked_human_representative(user_input):
    """
    Checks if the user input contains any keywords indicating a request to speak with a human representative.

    Parameters:
    user_input (str): The input from the user.

    Returns:
    bool: True if a keyword is found, False otherwise.
    """
    for keyword in hum_rep_keywords:
        if keyword in user_input:
            return True
    return False


def save_details(full_name, email, phone):
    """
    Saves user details to a CSV file.

    Parameters:
    full_name (str): The full name of the user.
    email (str): The email address of the user.
    phone (str): The phone number of the user.
    """
    with open("user_info.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([full_name, email, phone])


def call_human_representative():
    """
    Handles the process of escalating the conversation to a human representative by collecting user details.
    """
    verification_question = (
        "Chatbot: It seems you prefer to talk to a human representative. If that is the case, "
        "please let me know."
    )
    chat_history.append({"role": "assistant", "content": verification_question})
    print(verification_question)
    verification_ans = input("You: ")
    chat_history.append({"role": "user", "content": verification_ans})
    verification_ans = verification_ans.lower()
    for keyword in verification_ans_keywords:
        if keyword in verification_ans:
            name_ask = "Chatbot: Please provide your full name: "
            print(name_ask)
            full_name = input("You: ")
            email_ask = "Chatbot: Please provide your email address: "
            print(email_ask)
            email = input("You: ")
            phone_ask = "Chatbot: Please provide your phone number: "
            print(phone_ask)
            phone = input("You: ")
            save_details(full_name, email, phone)
            post = "Chatbot: Ok! Our crew will contact you as soon as possible! Anything else?"
            print(post)
            chat_history.append({"role": "assistant", "content": name_ask})
            chat_history.append({"role": "user", "content": full_name})
            chat_history.append({"role": "assistant", "content": email_ask})
            chat_history.append({"role": "user", "content": email})
            chat_history.append({"role": "assistant", "content": phone_ask})
            chat_history.append({"role": "user", "content": phone})
            chat_history.append({"role": "assistant", "content": post})
            return


def asked_order_status(user_input):
    """
    Checks if the user input contains any keywords indicating a request to check order status.

    Parameters:
    user_input (str): The input from the user.

    Returns:
    bool: True if a keyword is found, False otherwise.
    """
    for keyword in order_status_keywords:
        if keyword in user_input:
            return True
    return False


def call_order_check():
    """
    Handles the process of checking the order status by interacting with the database.
    """
    verification_question = (
        "Chatbot: It seems you like to check the status of your order. If that is the case, "
        "please let me know."
    )
    chat_history.append({"role": "assistant", "content": verification_question})
    print(verification_question)
    verification_ans = input("You: ")
    chat_history.append({"role": "user", "content": verification_ans})
    verification_ans = verification_ans.lower()
    for keyword in verification_ans_keywords:
        if keyword in verification_ans:
            order_number_ask = "Chatbot: Please provide your order id: "
            print(order_number_ask)
            order_number = input("You: ")
            conn = sqlite3.connect("orders.db")
            chat_history.append({"role": "assistant", "content": order_number_ask})
            chat_history.append({"role": "user", "content": order_number})
            cursor = conn.cursor()
            cursor.execute(
                "SELECT status FROM orders WHERE order_number = ?", (order_number,)
            )
            result = cursor.fetchone()
            conn.close()
            if result:
                status = result[0]
                ans = f"Chatbot: The status of order number {order_number} is {status}."
                print(ans)
                chat_history.append({"role": "assistant", "content": ans})
            else:
                ans = f"Chatbot: Order number {order_number} does not exist in the database."
                print(ans)
                chat_history.append({"role": "assistant", "content": ans})


def start_conversation():
    """
    Starts the chatbot conversation loop, handling user inputs and generating responses.
    """
    chatbot = ChatBot(os.getenv("OPENAI_API_KEY"))
    pre = "Chatbot: Hello! How can i help you today?"
    print(pre)
    chat_history.append({"role": "user", "content": pre})
    while True:
        user_input = input("You: ")
        chat_history.append({"role": "user", "content": user_input})
        if asked_human_representative(user_input.lower()):
            call_human_representative()
            continue
        if asked_order_status(user_input.lower()):
            call_order_check()
            continue
        response_text = chatbot.get_response(chat_history)
        chat_history.append({"role": "assistant", "content": response_text})
        print(f"Chatbot: {response_text}")


# Entry point for the script
if __name__ == "__main__":
    start_conversation()
