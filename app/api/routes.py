from fastapi import APIRouter, HTTPException, status
from app.schemas.prediction import ChatRequest, ChatResponse
from app.services.ai_service import generar_respuesta_tutor

router = APIRouter()

@router.get("/health", summary="Verificar estado del servicio", tags=["Monitoreo"])
def health_check():
    return {"status": "activo", "servicio": "EdubotAI API"}

@router.get("/metadata", summary="Obtener metadatos", tags=["Monitoreo"])
def get_metadata():
    return {
        "proyecto": "EdubotAI",
        "proposito": "Proveer tutoría personalizada y predicción de deserción académica.",
        "version": "1.0.0",
        "tecnologias": ["FastAPI", "Groq Cloud API", "Pickle"],
        "modelos": ["modelo_edubot.pkl", "llama-3.3-70b-versatile"]
    }

@router.post("/chat", response_model=ChatResponse, summary="Ejecutar capacidad inteligente", tags=["IA Tutor"])
def chat_ia(request: ChatRequest):
    if request.modulo not in ["C++", "Data Science", "Web"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Módulo no válido. Seleccione: C++, Data Science o Web."
        )

    try:
        respuesta_generada = generar_respuesta_tutor(request.modulo, request.mensaje)

        return ChatResponse(
            respuesta_ia=respuesta_generada,
            puntuacion_actualizada=5,
            estado="Success"
        )
    except RuntimeError as re:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(re))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error interno con la IA: {str(e)}")