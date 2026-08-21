import os
import time
from functools import lru_cache
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("No se encontró GROQ_API_KEY en las variables de entorno.")

# Cliente inicializado una sola vez (no en cada llamada)
client = Groq(api_key=GROQ_API_KEY)


# 1. Caché: Guarda en memoria las últimas 100 respuestas.
#    Acelera el bot a 0.01ms en preguntas repetidas (mismo modulo + mismo mensaje).
@lru_cache(maxsize=100)
def generar_respuesta_ia_cacheada(modulo: str, mensaje: str) -> str:
    t0 = time.perf_counter()

    prompt = f"Actúa como un tutor para un estudiante del módulo {modulo}. Responde a su duda: {mensaje}"

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Eres Edubot. Responde de forma directa, educada y en menos de 100 palabras."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,  # 3. PROTECCIÓN: Límite estricto de tokens por respuesta
            temperature=0.5
        )
        respuesta = response.choices[0].message.content
    except Exception as e:
        respuesta = "Edubot está procesando muchas consultas. Por favor, intenta de nuevo en unos segundos."

    t1 = time.perf_counter()
    inference_ms = (t1 - t0) * 1000
    print(f'{{"event": "ai_inference", "model_version": "llama-3.3-70b-versatile", "inference_ms": {inference_ms:.2f}}}')

    return respuesta


def generar_respuesta_tutor(modulo: str, mensaje: str) -> str:
    # Función principal (mantiene el mismo nombre que usa el resto del proyecto)
    # que llama a la versión con caché.
    return generar_respuesta_ia_cacheada(modulo, mensaje)