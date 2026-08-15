import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generar_respuesta_tutor(modulo: str, mensaje: str) -> str:
    if not GROQ_API_KEY:
        raise RuntimeError("No se encontró GROQ_API_KEY en las variables de entorno.")

    client = Groq(api_key=GROQ_API_KEY)
    prompt = f"Actúa como un tutor para un estudiante del módulo {modulo}. Responde a su duda: {mensaje}"

    t0 = time.perf_counter()
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=256,
        )
    finally:
        t1 = time.perf_counter()
        inference_ms = (t1 - t0) * 1000
        print(f'{{"event": "ai_inference", "model_version": "llama-3.3-70b-versatile", "inference_ms": {inference_ms:.2f}}}')

    return chat_completion.choices[0].message.content