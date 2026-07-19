from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import os
from dotenv import load_dotenv
from groq import Groq

# Cargar variables de entorno desde el archivo .env de forma segura
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Validar que la clave exista para evitar errores en producción
if not GROQ_API_KEY:
    raise RuntimeError("No se encontró GROQ_API_KEY en las variables de entorno.")

# Inicializar cliente de Groq
client = Groq(api_key=GROQ_API_KEY)

app = FastAPI(
    title="EdubotAI API",
    description="API inteligente para el tutor virtual EdubotAI.",
    version="1.0.0"
)

from fastapi.responses import RedirectResponse

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

# --- ESQUEMAS DE VALIDACIÓN (Pydantic) ---
class ChatRequest(BaseModel):
    estudiante_id: str = Field(..., example="UGB2026")
    mensaje: str = Field(..., min_length=2, example="¿Qué es una variable en Data Science?")
    modulo: str = Field(..., example="Data Science")

class ChatResponse(BaseModel):
    respuesta_ia: str
    puntuacion_actualizada: int
    estado: str

# --- ENDPOINTS REQUERIDOS ---

@app.get("/health", summary="Verificar estado del servicio")
def health_check():
    return {"status": "activo", "servicio": "EdubotAI API"}

@app.get("/metadata", summary="Obtener metadatos")
def get_metadata():
    return {
        "proyecto": "EdubotAI",
        "proposito": "Proveer tutoría personalizada y predicción de deserción académica.",
        "version": "1.0.0",
        "tecnologias": ["FastAPI", "Groq Cloud API", "Pickle"],
        "modelos": ["modelo_edubot.pkl", "llama-3.3-70b-versatile"]
    }

@app.post("/chat", response_model=ChatResponse, summary="Ejecutar capacidad inteligente")
def chat_ia(request: ChatRequest):
    try:
        if request.modulo not in ["C++", "Data Science", "Web"]:
            raise HTTPException(status_code=400, detail="Módulo no válido. Seleccione: C++, Data Science o Web.")

        # Consumiendo la API de Groq real
        prompt = f"Actúa como un tutor para un estudiante del módulo {request.modulo}. Responde a su duda: {request.mensaje}"
        
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile", 
            temperature=0.5,
            max_tokens=256,
        )
        
        respuesta_generada = chat_completion.choices[0].message.content

        return ChatResponse(
            respuesta_ia=respuesta_generada,
            puntuacion_actualizada=5,
            estado="Success"
        )
        
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno con la IA: {str(e)}")