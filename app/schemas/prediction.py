from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    estudiante_id: str = Field(..., json_schema_extra={"example": "UGB2026"})
    mensaje: str = Field(..., min_length=2, json_schema_extra={"example": "¿Qué es una variable en Data Science?"})
    modulo: str = Field(..., json_schema_extra={"example": "Data Science"})

class ChatResponse(BaseModel):
    respuesta_ia: str
    puntuacion_actualizada: int
    estado: str