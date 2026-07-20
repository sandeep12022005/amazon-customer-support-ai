from datetime import datetime
from database.mongodb import chat_collection


def save_chat(session_id, role, message, intent, agent):

    chat_collection.insert_one({

        "session_id": session_id,

        "role": role,

        "message": message,

        "intent": intent,

        "agent": agent,

        "timestamp": datetime.utcnow()

    })


def load_chat(session_id):

    docs = chat_collection.find(

        {

            "session_id": session_id

        }

    )

    history = ""

    for doc in docs:

        history += f"{doc['role']}: {doc['message']}\n"

    return history