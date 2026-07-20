from rag.retriever import retrieve_context
from services.gemini_service import ask_gemini


def returns_agent(message, history):

    context = retrieve_context(
        message,
        [
            "returns",
            "products"
        ]
    )

    prompt = f"""
You are an Amazon Returns Specialist.

Conversation History:

{history}

Company Documentation:

{context}

Customer Question:

{message}

Instructions:

1. Use ONLY the documentation.
2. If multiple documents are available, combine them.
3. Do not invent policies.
4. If information is missing, clearly say so.
5. Answer professionally.
"""

    return ask_gemini(prompt)