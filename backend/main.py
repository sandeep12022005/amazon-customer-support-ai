from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat import router as chat_router
from api.history import router as history_router   # NEW
from api.analytics import router as analytics_router

app = FastAPI(title="Amazon Customer Support AI")
app.include_router(analytics_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Chat API
app.include_router(chat_router)

# History API
app.include_router(history_router)

@app.get("/")
def home():
    return {
        "message": "Amazon Customer Support AI Backend Running"
    }