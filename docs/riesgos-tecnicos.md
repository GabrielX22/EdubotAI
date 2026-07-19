Riesgos Técnicos y Deuda Técnica

Categoría| Riesgo o Deuda Técnica| Probabilidad| Impacto| Mitigación Propuesta

Dependencias| Dependencia de ActivePieces| Alta| Alto| Migrar gradualmente parte de la lógica a FastAPI

Datos| Almacenamiento temporal de información| Alta| Alto| Evaluar persistencia futura

IA| Caída o lentitud de Groq Cloud| Media| Alto| Manejar errores y reintentos básicos

Código| Ausencia de pruebas automatizadas| Alta| Alto| Crear pruebas básicas

Seguridad| Gestión manual de credenciales| Media| Alto| Uso de variables de entorno

Despliegue| Falta de Docker| Media| Medio| Crear contenedor básico

Monitoreo| Ausencia de registros estructurados| Alta| Medio| Implementar logs simples

Equipo| Dependencia del conocimiento individual| Media| Medio| Mejorar documentación

Modelo| Posible desactualización del modelo predictivo| Baja| Medio| Revisar y actualizar periódicamente

Servicios Externos| Dependencia de Internet| Alta| Medio| Documentar limitación y manejo de errores

---

Resumen

Actualmente los riesgos más importantes están relacionados con la dependencia de ActivePieces, la falta de persistencia de datos y la ausencia de pruebas automatizadas. Estas áreas serán abordadas progresivamente durante las siguientes semanas del proyecto.