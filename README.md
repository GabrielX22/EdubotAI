EdubotAI

Equipo 4

Integrantes

- Gabriel Eduardo Henriquez Gonzalez

- Melvin Josué Pereira Amaya

- Alexis Manuel Calix Magaña

---

Descripción del Problema

Los estudiantes de Ciencias de la Computación presentan dificultades para obtener retroalimentación inmediata fuera del aula, provocando desmotivación y riesgo de deserción académica.

La falta de acompañamiento constante en temas como programación, desarrollo web y ciencia de datos dificulta el aprendizaje autónomo y limita la capacidad de los estudiantes para resolver dudas en tiempo real.

---

Usuarios Beneficiarios

- Estudiantes UGB

- Estudiantes autodidactas

- Docentes de apoyo

---

Descripción General de la Solución

EdubotAI es un tutor inteligente desplegado en Telegram que ofrece:

- Tutoría personalizada

- Evaluaciones gamificadas

- Generación de explicaciones con IA

- Predicción de riesgo de deserción

La aplicación permite a los estudiantes interactuar mediante Telegram para resolver dudas, responder cuestionarios y recibir retroalimentación inmediata utilizando Inteligencia Artificial.

---

Inteligencia Artificial Utilizada

IA Generativa

Servicio:

- Groq Cloud API

Funciones:

- Generación de explicaciones

- Resolución de dudas

- Generación de preguntas

IA Predictiva

Archivos:

modelo_edubot.pkl

scaler_edubot.pkl

Función:

Predicción de riesgo de deserción estudiantil basada en patrones de interacción.

---

Datos de Entrada

- Comandos Telegram

- Respuestas del estudiante

- Historial de sesión

- Selección de módulos

Datos de Salida

- Explicaciones personalizadas

- Preguntas de evaluación

- Puntuación acumulada

- Predicción de riesgo

---

Arquitectura

Arquitectura Actual

Ver:

docs/arquitectura-actual.md

Arquitectura Objetivo

Ver:

docs/arquitectura-objetivo.md

---

Tecnologías

- Telegram Bot API

- ActivePieces

- Groq Cloud

- Python

- JavaScript

- Pickle

- FastAPI (planeado)

- PostgreSQL (planeado)

---

Instalación y Ejecución

Variables de entorno

TELEGRAM_BOT_TOKEN=

GROQ_API_KEY=

ACTIVEPIECES_WEBHOOK_URL=

Archivos necesarios

modelo_edubot.pkl

scaler_edubot.pkl

requirements.txt

Procfile

nixpacks.toml

Pasos

1. Configurar Telegram Bot.

2. Configurar Groq API.

3. Importar workflow ActivePieces.

4. Cargar modelos .pkl.

5. Ejecutar workflow.

6. Enviar /start.

---

Limitaciones Conocidas

- Dependencia de internet.

- Dependencia de Groq Cloud.

- Dependencia de ActivePieces.

- Almacenamiento temporal.

- Sin pruebas automatizadas.

- Sin Docker.

- Sin base de datos persistente.

- Manejo limitado de errores.

---

Documentación Técnica

- docs/diagnostico-semana-1.md

- docs/arquitectura-actual.md

- docs/arquitectura-objetivo.md

- docs/riesgos-tecnicos.md

- docs/plan-mejora.md

- docs/evidencias.md

---

Evidencias de Funcionamiento

Las evidencias del prototipo se encuentran documentadas en:

docs/evidencias.md

Incluyen:

- Mensaje de bienvenida del bot.

- Navegación entre módulos.

- Respuestas generadas por IA.

- Sistema de puntuación.

- Ejecución exitosa del workflow de ActivePieces.

---

Plan de Mejora (Semanas 2–6)

Semana| Objetivo

2| Organizar el proyecto y crear una API básica

3| Realizar pruebas básicas del sistema

4| Preparar despliegue sencillo con Docker

5| Agregar registros básicos de errores y tiempos de respuesta

6| Actualizar documentación y preparar la defensa final

Para más detalles consultar:

docs/plan-mejora.md

---

Estado Actual

Prototipo funcional validado en Telegram.

- Menús interactivos

- IA generativa

- Gamificación

- Predicción de deserción

- Latencia promedio menor a 1.5 segundos

---

Licencia

Proyecto académico desarrollado para el Módulo 4 – Desarrollo de Aplicaciones con IA.