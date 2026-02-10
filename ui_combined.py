# ui_combined.py
import threading
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import gradio as gr
import requests

# --- FastAPI ---
app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    user_msg = request.message
    # Ici tu peux appeler GPT ou mettre une réponse test
    return {"response": f"Réponse simulée : {user_msg}"}

def start_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)

threading.Thread(target=start_api, daemon=True).start()

# --- Gradio ---
def chat_with_bot(user_message):
    response = requests.post("http://127.0.0.1:8000/chat", json={"message": user_message})
    return response.json()["response"]

interface = gr.Interface(
    fn=chat_with_bot,
    inputs=gr.Textbox(lines=2, placeholder="Posez votre question..."),
    outputs="text",
    title="🤖 AI Customer Support Chatbot",
    description="Assistant intelligent pour répondre aux FAQs clients"
)

if __name__ == "__main__":
    interface.launch()
