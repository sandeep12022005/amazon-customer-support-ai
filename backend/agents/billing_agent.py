from rag.retriever import retrieve_context
from services.gemini_service import ask_gemini


def billing_agent(message, history):

    context = retrieve_context(
    message,
    [
        "billing",
        "orders"
    ]
)

    prompt = f"""
You are Amazon Billing Support.

Previous Conversation:

{history}

Company Documentation:

{context}

Customer Question:

{message}

Answer only using the documentation.
"""

    return ask_gemini(prompt)