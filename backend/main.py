from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.utils import clean_email_text
from backend.prompt_engineering import build_prompt

app = FastAPI()

# Allow frontend (on different port) to access this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    email: str
    tone: str
    length: str

# Before Regex performed to clean email input: 

# @app.post("/generate")
# async def generate_reply(request: EmailRequest):
    # Dummy logic for now
    # reply = f"Thanks for your email! Here's a {request.tone.lower()} and {request.length.lower()} reply."
    # return {"reply": reply}

# Before prompt engineering: 

# @app.post("/generate")
# async def generate_reply(request: EmailRequest):
    # cleaned_email = clean_email_text(request.email)
    # reply = f"Thanks for your message: '{cleaned_email[:60]}...' Here's a {request.tone.lower()} and {request.length.lower()} reply."
    # return {"reply": reply}

@app.post("/generate")
async def generate_reply(request: EmailRequest):
    cleaned_email = clean_email_text(request.email)
    prompt = build_prompt(cleaned_email, request.tone, request.length)
    
    # Dummy stand-in for actual LLM call
    reply = f"(LLM would respond here based on this prompt):\n\n{prompt}"
    return {"reply": reply}
