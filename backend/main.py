from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat import router as chat_router
from api.history import router as history_router
from api.analytics import router as analytics_router

app = FastAPI(title="Amazon Customer Support AI")

# ---------------- CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000"
        # Later add your Vercel URL here
        # "https://your-project.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Routers ----------------

app.include_router(chat_router)
app.include_router(history_router)
app.include_router(analytics_router)

# ---------------- Home ----------------

@app.get("/")
def home():
    return {
        "message": "Amazon Customer Support AI Backend Running"
    }
@app.get("/health")
def health():
    return {"status": "ok"}