Evidencias de Funcionamiento

Evidencia 1: Inicio del Bot

Entrada

/start

Salida Esperada

Bienvenido a EdubotAI

Seleccione un módulo:

- C++

- Data Science

- Web

---

Evidencia 2: Navegación de Módulos

El usuario selecciona una ruta de aprendizaje y el sistema muestra contenido o preguntas relacionadas con el tema elegido.

---

Evidencia 3: Respuesta Generada por IA

El usuario realiza una consulta académica y Groq Cloud genera una explicación personalizada basada en el contexto de la conversación.

---

Evidencia 4: Sistema de Puntuación

Cuando una respuesta es correcta, el sistema incrementa automáticamente la puntuación del estudiante.

Ejemplo:

✅ Respuesta correcta

Puntuación actual: 5 puntos

---

Evidencia 5: Ejecución Correcta del Workflow

Registro simplificado del flujo:

Telegram Trigger

Storage Get

Router

Groq Cloud

Storage Set

Send Message

Estado: Success

---

Evidencia General

Actualmente el prototipo permite:

- Interacción mediante Telegram.

- Generación de respuestas con IA.

- Navegación entre módulos.

- Evaluación básica.

- Sistema de puntuación.

- Predicción de riesgo de deserción.

Todo ello utilizando el workflow implementado en ActivePieces.