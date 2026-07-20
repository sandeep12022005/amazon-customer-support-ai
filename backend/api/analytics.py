from fastapi import APIRouter
from database.mongodb import chat_collection

router = APIRouter()


@router.get("/analytics")
def analytics():

    total_messages = chat_collection.count_documents({})

    sessions = len(chat_collection.distinct("session_id"))

    intents = list(
        chat_collection.aggregate([
            {
                "$group": {
                    "_id": "$intent",
                    "count": {"$sum": 1}
                }
            }
        ])
    )

    agents = list(
        chat_collection.aggregate([
            {
                "$group": {
                    "_id": "$agent",
                    "count": {"$sum": 1}
                }
            }
        ])
    )

    return {
        "total_messages": total_messages,
        "total_sessions": sessions,
        "intents": intents,
        "agents": agents
    }