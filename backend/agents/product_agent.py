from rag.retriever import retrieve_context
from services.gemini_service import ask_gemini


def product_agent(message, history):

    context = retrieve_context(
    message,
    [
        "products",
        "general"
    ]
)

    prompt = f"""
You are Amazon Product Expert.

Previous Conversation:

{history}

Company Documentation:

{context}

Customer Question:

{message}

Answer only using the documentation.
"""

    return ask_gemini(prompt)