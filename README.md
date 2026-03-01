# 🛡 Simulación de Incidente de Ciberseguridad en Entorno Clínico

## 📌 Descripción del Proyecto

Este proyecto presenta la construcción y validación de un entorno controlado que simula la infraestructura tecnológica de una clínica modernizada con:

- Windows Server (simulado)
- API REST
- SQL Server
- Active Directory (conceptual)
- Segmentación de red (DMZ e interna)

El objetivo fue analizar un escenario de amenaza avanzada en el que un atacante explota una vulnerabilidad en la API y posteriormente despliega ransomware en la red interna.

El laboratorio integra aspectos técnicos, estratégicos y operativos de ciberseguridad.

---

## 🎯 Objetivos

- Implementar un MVP funcional utilizando Docker.
- Aplicar el modelo de Defensa en Profundidad.
- Validar controles mediante pentesting desde Kali Linux.
- Simular un ataque de ingeniería social.
- Diseñar un Plan de Respuesta a Incidentes.
- Realizar un análisis de gestión de riesgos.
- Simular un ejercicio de forense digital.
- Integrar inteligencia de amenazas (CTI).

---

## 🏗 Arquitectura del MVP

El entorno está compuesto por:

- **Reverse Proxy (Nginx)** – Punto de entrada expuesto (puerto 8081).
- **API REST (Flask)** – Servicio interno.
- **SQL Server** – Base de datos aislada en red interna.
- **Segmentación Docker Networks:**
  - `dmz`
  - `internal`

Principios aplicados:

- Segmentación de red
- Minimización de superficie de ataque
- Rate limiting
- Aislamiento de base de datos
- Automatización básica de verificación

---

## 🐳 Despliegue del Entorno

### 1️⃣ Clonar repositorio

```bash
git clone <URL_DEL_REPO>
cd clinic-mvp
