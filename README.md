# 🤖 EduBot AI — Tutor Virtual Inteligente

> Chatbot educativo basado en Inteligencia Artificial que detecta el riesgo de deserción estudiantil y activa un Modo Refuerzo personalizado para cada estudiante.

[![CI - EduBot API](https://github.com/MelvinAmaya/edubot-api/actions/workflows/ci.yml/badge.svg)](https://github.com/MelvinAmaya/edubot-api/actions/workflows/ci.yml)

---

## Información general

**Módulo:** Módulo 4 - Desarrollo de Aplicaciones con IA    
**Nombre del equipo:** EduBot AI  
**Integrantes:**

- Melvin Josué Pereira Amaya
- Gabriel Eduardo Henriquez Gonzalez
- Alexis Manuel Caliz Magaña

---

## 📋 Descripción

EduBot AI es un sistema educativo inteligente que opera a través de Telegram. Combina un flujo de automatización en Activepieces con dos APIs especializadas:

- **API de Predicción de Deserción** → analiza el comportamiento del estudiante y calcula la probabilidad de abandono del curso.
- **API de Lenguaje (Groq + LLM)** → genera explicaciones simplificadas cuando el estudiante está en riesgo.

Cuando un estudiante falla un quiz o muestra señales de desenganche, el sistema interviene automáticamente con contenido adaptado a su nivel de comprensión.

---

## 🏗️ Arquitectura del sistema

```
Estudiante
    ↓  mensaje por Telegram
Bot de Telegram
    ↓
Activepieces (orquestador del flujo)
    ↓                          ↓
API de Predicción         API de Lenguaje
(Regresión Logística)     (Groq + LLM)
    ↓                          ↓
¿Pd > 0.65?            Explicación simplificada
    ↓ true
Modo Refuerzo → estudiante recibe ayuda personalizada
```

### Componentes

| Componente | Tecnología | Repositorio / URL |
|---|---|---|
| Bot de Telegram | Activepieces | Este repositorio |
| API de Predicción | FastAPI + scikit-learn | [MelvinAmaya/edubot-api](https://github.com/MelvinAmaya/edubot-api) |
| API de Lenguaje | Groq + LLM | Este repositorio |
| Base de datos | Supabase (PostgreSQL) | Configurado en variables de entorno |

---

## 🚀 Despliegue con Docker (Semana 4)

Este proyecto está preparado para ejecutarse mediante contenedores Docker. Sigue estos pasos para levantarlo en cualquier entorno limpio.

### Requisitos previos

- [Docker](https://www.docker.com/get-started) instalado
- Cuenta en [Groq](https://console.groq.com/) para obtener la API Key

### Paso 1 — Clonar el repositorio

```bash
git clone https://github.com/GabrielX22/EdubotAI.git
cd EdubotAI
```

### Paso 2 — Configurar variables de entorno

Copia el archivo de ejemplo y coloca los valores reales:

```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

Abre el archivo `.env` y reemplaza los valores:

```env
GROQ_API_KEY=tu_clave_real_de_groq
APP_ENV=production
API_PORT=8000
```

> ⚠️ Nunca subas el archivo `.env` al repositorio. Ya está incluido en el `.gitignore`.

### Paso 3 — Construir la imagen Docker

```bash
docker build -t edubotai-app .
```

### Paso 4 — Ejecutar el contenedor

```bash
docker run --name edubot -p 8000:8000 --env-file .env edubotai-app
```

### Paso 5 — Verificar que funciona

Abre en el navegador:

```
http://localhost:8000/health
```

Debe responder:

```json
{
  "status": "ok"
}
```

---

## 🔧 Instalación local (sin Docker)

```bash
# Clonar el repositorio
git clone https://github.com/GabrielX22/EdubotAI.git
cd EdubotAI

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con los valores reales

# Ejecutar
uvicorn main:app --reload --port 8000
```

---

## 🌐 APIs del proyecto

### API de Predicción de Deserción

Microservicio independiente que calcula la probabilidad de abandono del estudiante.

- **Repositorio:** [MelvinAmaya/edubot-api](https://github.com/MelvinAmaya/edubot-api)
- **URL en producción:** `https://edubot-api-db1w.onrender.com`
- **Documentación:** `https://edubot-api-db1w.onrender.com/docs`

**Endpoint principal:**

```
POST https://edubot-api-db1w.onrender.com/predict
Header: X-API-Key: {clave del equipo}
```

**Respuesta clave para el flujo:**

```json
{
  "activar_modo_refuerzo": true,
  "nivel_riesgo": "alto",
  "confidence": 0.87
}
```

Cuando `activar_modo_refuerzo` es `true`, Activepieces llama a la API de lenguaje para generar la explicación del Modo Refuerzo.

---

## 📁 Estructura del repositorio

```
EdubotAI/
├── main.py                  # Punto de entrada principal
├── requirements.txt         # Dependencias de Python
├── .env.example             # Variables de entorno de ejemplo
├── .gitignore               # Archivos ignorados por Git
├── Dockerfile               # Configuración del contenedor Docker
└── README.md                # Este archivo
```

---

## 🔐 Variables de entorno

| Variable | Descripción | Obligatoria |
|---|---|---|
| `GROQ_API_KEY` | Clave de la API de Groq para el modelo de lenguaje | Sí |
| `APP_ENV` | Entorno de ejecución (`production` / `development`) | No |
| `API_PORT` | Puerto del servidor (por defecto 8000) | No |

---

## 🤝 Contribución

Este proyecto sigue un flujo de trabajo con ramas:

```bash
# Crear nueva rama para tu tarea
git checkout -b tipo/descripcion-corta

# Ejemplos:
git checkout -b feat/nueva-funcionalidad
git checkout -b fix/correccion-error
git checkout -b docs/actualizar-readme
```

Una vez terminado tu trabajo, abre un **Pull Request** hacia `main` para que el equipo lo revise antes de hacer el merge.

---

## 👥 Equipo

| Integrante | Rol |
|---|---|
| Melvin Amaya | API de Predicción de Deserción + Documentación |
| Gabriel | Bot de Telegram + API de Lenguaje |
| Alexis | Plan de Infraestructura, Costos y Riesgos |

---

## 📚 Referencias

- [FastAPI](https://fastapi.tiangolo.com/)
- [Groq API](https://console.groq.com/docs)
- [Activepieces](https://www.activepieces.com/)
- [Supabase](https://supabase.com/)
- [Docker](https://docs.docker.com/)
- [scikit-learn](https://scikit-learn.org/)
