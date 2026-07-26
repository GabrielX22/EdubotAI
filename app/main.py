from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.api.routes import router

app = FastAPI(
    title="EdubotAI API",
    description="API inteligente para el tutor virtual EdubotAI.",
    version="1.0.0"
)

# Redirección automática a la documentación interactiva
@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")

# Incluir las rutas modularizadas
app.include_router(router)