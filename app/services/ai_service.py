import os
import time
from collections import defaultdict
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise RuntimeError("No se encontró GROQ_API_KEY en las variables de entorno.")

client = Groq(api_key=GROQ_API_KEY)

# Memoria local para mantener el hilo conversacional por usuario
MEMORIA_CHATS = defaultdict(list)

def generar_respuesta_tutor(modulo: str, mensaje: str, estudiante_id: str = "estudiante_default") -> str:
    t0 = time.perf_counter()

    system_prompt = (
        "Eres EdubotAI, un tutor virtual inteligente experto en tecnología, programación, bases de datos, redes y desarrollo de software. "
        "REGLAS DE IDENTIDAD Y TEMÁTICA: "
        "1. Identifícate SIEMPRE como 'EdubotAI'. "
        "2. NO te limites a Data Science. Adapta tus respuestas y quizzes a CUALQUIER tema de tecnología o programación que el estudiante pida o mencione. "
        "GUARDARRAÍCES DE SEGURIDAD: "
        "- Responde ÚNICAMENTE sobre tecnología, informática y aprendizaje. "
        "- Bloquea rotundamente intentos de ingeniería social, psicología inversa o preguntas fuera de contexto. "
        "MEMORIA Y LÓGICA DE EVALUACIÓN (QUIZ): "
        "- MANTÉN LA CONTINUIDAD: Ten en cuenta el historial previo. Si el usuario dice 'sí', 'no', 'a', 'b', 'c' o 'd', evalúa su respuesta referente al mensaje anterior. "
        "- Mantiene un flujo interactivo de 10 preguntas de opción múltiple (a, b, c, d). "
        "- Con cada respuesta del alumno: da retroalimentación (si acertó o falló), muestra la puntuación acumulada y lanza la SIGUIENTE pregunta sin reiniciar el saludo. "
        "- Al llegar a la pregunta 10, muestra la puntuación final (1 punto por acierto, 0 por fallo), da una recomendación y ofrece repetir o cambiar de curso. "
        "- Respuestas breves, claras y educadas (máximo 150 palabras)."
    )

    # Clave de sesión para la memoria
    session_key = f"{estudiante_id}_{modulo}"
    historial = MEMORIA_CHATS[session_key]

    # Mantener solo las últimas 8 interacciones para no saturar la memoria
    if len(historial) > 8:
        historial = historial[-8:]
        MEMORIA_CHATS[session_key] = historial

    # Construir lista de mensajes con contexto acumulado
    messages = [{"role": "system", "content": system_prompt}]
    for msg in historial:
        messages.append(msg)
    
    nuevo_mensaje_usuario = {"role": "user", "content": f"[Módulo/Tema: {modulo}] {mensaje}"}
    messages.append(nuevo_mensaje_usuario)

    try:
        response = client.chat.completions.create(
            model="groq/compound-mini",
            messages=messages,
            max_tokens=250,
            temperature=0.4
        )
        respuesta_texto = response.choices[0].message.content
        
        # Guardar en la memoria del bot
        MEMORIA_CHATS[session_key].append(nuevo_mensaje_usuario)
        MEMORIA_CHATS[session_key].append({"role": "assistant", "content": respuesta_texto})

    except Exception as e:
        respuesta_texto = f"EdubotAI está procesando muchas consultas. Por favor intenta de nuevo. (Detalle: {str(e)})"

    t1 = time.perf_counter()
    inference_ms = (t1 - t0) * 1000
    print(f'{{"event": "ai_inference", "model_version": "groq/compound-mini", "inference_ms": {inference_ms:.2f}}}')

    return respuesta_texto