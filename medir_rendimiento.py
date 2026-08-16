import requests
import time
import statistics

URL = "http://127.0.0.1:8000/chat"

# ¡El cambio clave! Usamos un payload que sí pasa tus validaciones
PAYLOAD = {
    "estudiante_id": "UGB2026",
    "mensaje": "¿Qué es una variable?",
    "modulo": "Data Science"
}
NUM_REQUESTS = 20

tiempos = []
errores = 0

print(f"Ejecutando {NUM_REQUESTS} peticiones a {URL}...\n")

for i in range(NUM_REQUESTS):
    try:
        # Aumentamos el timeout a 15 seg por si Groq tarda
        response = requests.post(URL, json=PAYLOAD, timeout=15) 
        
        if response.status_code == 200:
            tiempo = float(response.headers.get("X-Process-Time-Ms", 0))
            tiempos.append(tiempo)
            print(f"[{i+1}/{NUM_REQUESTS}] Éxito - Tiempo: {tiempo:.2f} ms")
        else:
            print(f"[{i+1}/{NUM_REQUESTS}] Error - Status: {response.status_code}")
            errores += 1
            
    except Exception as e:
        print(f"[{i+1}/{NUM_REQUESTS}] Fallo de conexión: {e}")
        errores += 1
        
    # Pausa de 1 segundo entre cada petición para evitar que Groq nos bloquee (Rate Limit)
    time.sleep(1) 

print("\n--- RESULTADOS LÍNEA BASE ---")
print(f"Peticiones exitosas: {len(tiempos)}")
print(f"Tasa de error: {(errores/NUM_REQUESTS)*100}%")

if tiempos:
    tiempos.sort()
    p50 = statistics.median(tiempos)
    p95 = tiempos[int(len(tiempos) * 0.95) - 1]
    max_t = max(tiempos)
    
    print(f"p50 (Mediana): {p50:.2f} ms")
    print(f"p95 (Cola lenta): {p95:.2f} ms")
    print(f"Tiempo Máximo: {max_t:.2f} ms")
else:
    print("No se pudo calcular métricas porque todas las peticiones fallaron.")