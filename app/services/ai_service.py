import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Inicializamos el cliente de Groq
client = Groq(api_key=GROQ_API_KEY if GROQ_API_KEY else "dummy_key")

def generar_respuesta_tutor(modulo: str, mensaje: str) -> str:
    try:
        # Llamada directa y limpia a Groq
        response = client.chat.completions.create(
            model="groq/compound-mini",
            messages=[
                {"role": "system", "content": "Eres Edubot. Responde de forma directa, educada y en menos de 50 palabras."},
                {"role": "user", "content": f"Módulo: {modulo}. Duda: {mensaje}"}
            ],
            max_tokens=100,
            temperature=0.5
        )
        return response.choices[0].message.content
        
    except Exception as e:
        # Si hay un error, devolvemos el texto exacto del error para verlo en Swagger
        return f"[ERROR DE IA DETECTADO]: {str(e)}"