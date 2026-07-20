import os
import time
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# -----------------------------
# Load Environment Variables
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)

# -----------------------------
# Models (Fallback Order)
# -----------------------------
MODELS = [
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-flash-latest",
    "gemini-2.0-flash"
]


def ask_gemini(prompt: str) -> str:
    """
    Sends a prompt to Gemini.
    Automatically switches to another model if one is unavailable.
    """

    last_error = None

    for model in MODELS:

        try:

            print(f"\nUsing Model : {model}")

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            if response.text:
                return response.text

        except Exception as e:

            print(f"{model} failed : {e}")
            last_error = e
            time.sleep(2)

    return f"""
Sorry, the AI service is temporarily unavailable.

Reason:
{last_error}
"""