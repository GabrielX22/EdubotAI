# Plan de Infraestructura y Costos Iniciales (EdubotAI)

## 1. Plan de Infraestructura Mínima
* *Cómputo:* Despliegue de la API mediante contenedor Docker ejecutado en entorno PaaS (Render / Railway) o entorno simulado profesional.
* *Modelo IA:* Consumo de LLM mediante API externa (Groq Cloud).
* *Red:* Exposición del puerto 8000, consumo vía HTTP/REST.

## 2. Estimación de Costos (Supuestos Mensuales)
* *Servicio Web (Render Free Tier):* $0.00 / mes (Adecuado para prototipo).
* *API IA (Groq - Llama 3):* $0.00 / mes (Uso del Free Tier).
* *Base de Datos / Almacenamiento:* $0.00 / mes (No requerido en esta fase).
* *Costo Total Estimado:* $0.00 / mes.

## 3. Riesgos Técnicos Pendientes
1. *Límites de Rate-Limit:* Al usar la capa gratuita de Groq, solicitudes concurrentes altas podrían ser rechazadas.
2. *Cold Starts:* Plataformas PaaS gratuitas "duermen" la API tras inactividad, provocando demoras en la primera respuesta.
3. *Persistencia:* Actualmente el historial de chat no persiste si el contenedor se reinicia.