from fastapi import APIRouter
from pydantic import BaseModel

from agents.router import route_message

from services.chat_db import save_chat
from agents.intent_detector import detect_intent

router = APIRouter()


class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):

    intent = detect_intent(request.message)

    reply = route_message(

        request.session_id,

        request.message

    )

    save_chat(

        request.session_id,

        "User",

        request.message,

        intent,

        intent

    )

    save_chat(

        request.session_id,

        "Assistant",

        reply,

        intent,

        intent

    )

    return {

        "reply": reply

    }