import openai

openai.api_key = "entrer your code API"

SYSTEM_PROMPT = """
Tu es un assistant de support client professionnel.
Réponds clairement et poliment aux questions des clients.
Si tu ne connais pas la réponse, dis-le honnêtement.
"""

def get_gpt_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"]
