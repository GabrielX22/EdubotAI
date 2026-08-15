from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from app.api.routes import router
import time
import uuid

app = FastAPI(
    title="EdubotAI API",
    description="API inteligente para el tutor virtual EdubotAI.",
    version="1.0.0"
)

# ── Middleware de observabilidad ────────────────────────────
@app.middleware("http")
async def observe(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start = time.perf_counter()
 
    try:
        response = await call_next(request)
        status_code = response.status_code
    except Exception as e:
        status_code = 500
        print(f'{{"event": "error_controlado", "request_id": "{request_id}", "error_type": "{type(e).__name__}"}}')
        raise e
 
    duration_ms = (time.perf_counter() - start) * 1000
 
    # Inyectar trazabilidad en los headers
    response.headers["X-Request-ID"] = request_id
    response.headers["X-Process-Time-Ms"] = f"{duration_ms:.2f}"
 
    # Log estructurado en formato JSON (sin datos sensibles)
    print(f'{{"event": "request_completed", "request_id": "{request_id}", "method": "{request.method}", "path": "{request.url.path}", "status_code": {status_code}, "duration_ms": {duration_ms:.2f}}}')
 
    return response

# Redirección automática a la documentación interactiva
@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

# Incluir las rutas modularizadas
app.include_router(router)