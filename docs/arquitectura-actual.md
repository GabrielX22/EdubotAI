Arquitectura Actual

Actor Principal

Estudiante de la Universidad Gerardo Barrios (UGB).

---

Interfaz

Telegram Bot API.

---

Backend Actual

Workflow visual desarrollado en ActivePieces compuesto por 19 pasos.

Flujo General

1. Recepción de mensaje desde Telegram.

2. Obtención del estado de sesión.

3. Evaluación de la interacción.

4. Consulta a Groq Cloud.

5. Procesamiento de respuesta.

6. Actualización de puntuación.

7. Predicción de deserción.

8. Envío de respuesta al estudiante.

---

Componente de IA

IA Generativa

- Groq Cloud API

IA Predictiva

- modelo_edubot.pkl

- scaler_edubot.pkl

---

Datos Utilizados

- Mensajes enviados por el estudiante.

- Historial temporal de sesión.

- Puntuación acumulada.

- Estado de aprendizaje.

---

Servicios Externos

- Telegram Bot API

- Groq Cloud

---

Diagrama de Arquitectura Actual

flowchart LR

A[Estudiante]

B[Telegram]

C[ActivePieces]

D[Storage Temporal]

E[Groq Cloud]

F[Modelo Deserción]

G[Respuesta]

A --> B

B --> C

C --> D

C --> E

C --> F

D --> C

E --> C

F --> C

C --> G

G --> B

B --> A

---

Dependencias y Puntos Frágiles

- Dependencia de Internet.

- Dependencia de Telegram.

- Dependencia de Groq.

- Dependencia de ActivePieces.

- Datos almacenados temporalmente.

- Ausencia de reintentos automáticos ante errores.