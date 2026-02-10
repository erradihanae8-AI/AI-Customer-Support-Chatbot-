from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_gpt_response
from analytics import log_conversation

app = FastAPI(title="AI Customer Support Chatbot")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    bot_response = get_gpt_response(request.message)
    log_conversation(request.message, bot_response)
    return {"response": bot_response}
