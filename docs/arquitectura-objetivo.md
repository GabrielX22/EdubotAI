Arquitectura Objetivo

Objetivo General

Organizar mejor el proyecto para facilitar su mantenimiento y futuras mejoras sin cambiar completamente el funcionamiento actual.

---

Evolución Planeada

Semana 2

Crear una API básica con FastAPI para centralizar parte de la lógica.

Semana 3

Realizar pruebas básicas de funcionamiento.

Semana 4

Preparar ejecución mediante Docker.

Semana 5

Agregar registros simples de errores y tiempos de respuesta.

Semana 6

Completar documentación y preparar defensa técnica.

---

Componentes Futuros

Interfaz

- Telegram Bot API

Backend

- FastAPI

IA Generativa

- Groq Cloud

IA Predictiva

- modelo_edubot.pkl

Datos

- Almacenamiento temporal actual

- Posible integración futura con base de datos

---

Diagrama de Arquitectura Objetivo

flowchart LR

A[Usuario]

B[Telegram]

C[FastAPI]

D[Groq Cloud]

E[Modelo Deserción]

F[Logs Básicos]

A --> B

B --> C

C --> D

C --> E

C --> F

C --> B

B --> A

---

Beneficios Esperados

- Mejor organización del proyecto.

- Código más fácil de mantener.

- Pruebas más sencillas.

- Despliegue simplificado.

- Mejor documentación.