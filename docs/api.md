# Contratos de Integración - EdubotAI API

Esta documentación describe los endpoints desarrollados durante la Semana 2 para migrar la lógica hacia FastAPI, facilitando futuras pruebas y despliegues.

## 1. Endpoint: Estado de Salud
- **Ruta:** `/health`
- **Método:** `GET`
- **Propósito:** Verificar que el servicio está activo.
- **Respuesta Exitosa (200 OK):**
  ```json
  {
    "status": "activo",
    "servicio": "EdubotAI API"
  }