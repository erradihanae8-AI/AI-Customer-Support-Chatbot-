import json
import gradio as gr

# Charger le fichier JSON
with open("faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Fonction pour répondre aux questions
def get_answer(user_question):
    user_question = user_question.lower()
    for item in faq_data:
        if user_question in item["question"].lower():
            return item["answer"]
    return "Désolé, je n'ai pas compris votre question. Veuillez reformuler."

# Interface Gradio
interface = gr.Interface(
    fn=get_answer,
    inputs=gr.Textbox(lines=2, placeholder="Posez votre question..."),
    outputs="text",
    title="🤖 AI Customer Support Chatbot",
    description="Assistant intelligent pour répondre aux FAQs clients"
)

if __name__ == "__main__":
    interface.launch()
