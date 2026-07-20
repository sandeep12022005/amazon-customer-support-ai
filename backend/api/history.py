from fastapi import APIRouter
from database.mongodb import chat_collection

router = APIRouter()


@router.get("/history/{session_id}")

def history(session_id):

    chats = list(

        chat_collection.find(

            {

                "session_id": session_id

            },

            {

                "_id": 0

            }

        )

    )

    return chats