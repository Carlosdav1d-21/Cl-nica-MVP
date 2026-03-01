import json
import sys
import time
import urllib.request
import urllib.error

URL = "http://localhost:8081/health"
TIMEOUT_SECONDS = 5

def main():
    print(f"[healthcheck] Probando: {URL}")

    try:
        start = time.time()
        req = urllib.request.Request(URL, method="GET")
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            elapsed_ms = int((time.time() - start) * 1000)
            body = resp.read().decode("utf-8", errors="replace")

        print(f"[healthcheck] HTTP: {resp.status} | Tiempo: {elapsed_ms} ms")

        # Intento de parseo JSON (si falla, igual muestro el body)
        try:
            data = json.loads(body)
            print("[healthcheck] Respuesta JSON:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
        except json.JSONDecodeError:
            print("[healthcheck] Respuesta (no-JSON):")
            print(body)

        # Validación mínima esperada
        if resp.status == 200 and '"status"' in body and '"ok"' in body:
            print("[healthcheck] ✅ OK: Servicio disponible.")
            sys.exit(0)
        else:
            print("[healthcheck] ⚠️ Respuesta inesperada.")
            sys.exit(2)

    except urllib.error.URLError as e:
        print(f"[healthcheck] ❌ ERROR: No se pudo conectar. Detalle: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[healthcheck] ❌ ERROR inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
