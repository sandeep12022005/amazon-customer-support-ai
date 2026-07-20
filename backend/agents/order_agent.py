from rag.retriever import retrieve_context
from services.gemini_service import ask_gemini


def order_agent(message, history):

    context = retrieve_context(
    message,
    [
        "orders",
        "products"
    ]
)

    prompt = f"""
You are Amazon Order Support.

Previous Conversation:

{history}

Company Documentation:

{context}

Customer Question:

{message}

Answer only using the documentation.
"""

    return ask_gemini(prompt)