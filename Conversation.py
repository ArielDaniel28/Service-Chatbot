from ChatBot import *
from Company import *
import csv
import sqlite3
from dotenv import load_dotenv
import os


load_dotenv()

company = Company()
chat_history = [
    {
        "role": "system",
        "content": f""" You are a customer service chatbot for the company. You should 
only answer questions related to the company, its products, services, order status, return policies, and customer 
support. If you receive a question unrelated to the company, politely inform the user that you can only answer 
company-related questions. Company Policies: {company.get_policies_text()}. """,
    }
]
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
]
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
]


def asked_human_representative(user_input):
    for keyword in hum_rep_keywords:
        if keyword in user_input:
            return True
    return False


def save_details(full_name, email, phone):
    with open("user_info.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([full_name, email, phone])


def call_human_representative():
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
    for keyword in order_status_keywords:
        if keyword in user_input:
            return True
    return False


def call_order_check():
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


if __name__ == "__main__":
    start_conversation()
