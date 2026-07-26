import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generar_respuesta_tutor(modulo: str, mensaje: str) -> str:
    if not GROQ_API_KEY:
        raise RuntimeError("No se encontró GROQ_API_KEY en las variables de entorno.")

    client = Groq(api_key=GROQ_API_KEY)
    prompt = f"Actúa como un tutor para un estudiante del módulo {modulo}. Responde a su duda: {mensaje}"

    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        max_tokens=256,
    )
    
    return chat_completion.choices[0].message.content