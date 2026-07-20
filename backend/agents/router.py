from services.chat_db import load_chat
from agents.intent_detector import detect_intent

from agents.account_agent import account_agent
from agents.order_agent import order_agent
from agents.returns_agent import returns_agent
from agents.billing_agent import billing_agent
from agents.prime_agent import prime_agent
from agents.product_agent import product_agent
from agents.complaint_agent import complaint_agent
from agents.faq_agent import faq_agent


def route_message(session_id, message):

    history = load_chat(session_id)
    print("\n========== CHAT HISTORY ==========")
    print(history)
    print("==================================")

    intent = detect_intent(message)

    print("Intent:", intent)

    if intent == "account":
        return account_agent(message, history)

    elif intent == "orders":
        return order_agent(message, history)

    elif intent == "returns":
        return returns_agent(message, history)

    elif intent == "billing":
        return billing_agent(message, history)

    elif intent == "prime":
        return prime_agent(message, history)

    elif intent == "product":
        return product_agent(message, history)

    elif intent == "complaint":
        return complaint_agent(message, history)

    else:
        return faq_agent(message, history)