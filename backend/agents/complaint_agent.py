from rag.retriever import retrieve_context
from services.gemini_service import ask_gemini


def complaint_agent(message, history):

    context = retrieve_context(
    message,
    [
        "complaints",
        "orders",
        "returns"
    ]
)

    prompt = f"""
You are Amazon Complaint Resolution Officer.

Previous Conversation:

{history}

Company Documentation:

{context}

Customer Question:

{message}

Answer only using the documentation.

Always apologize politely.
"""

    return ask_gemini(prompt)