# 📅 Manejo de Citas con GoHighLevel (GHL) – Sala 3

Este ejercicio muestra cómo **crear, listar y manejar citas** usando la API de Calendarios de GHL, integrando un **endpoint webhook en Django** que recibe notificaciones cuando se crea una cita en la subcuenta **ReflexoPerú**.

---

## 🎯 Objetivos

- Crear una cita en GHL vía **POST /calendars/events/appointments**.  
- Listar citas en GHL vía **GET /calendars/events/appointments?calendarId=...**.  
- Guardar el `appointmentId` en una estructura local (SQLite en Django).  
- Probar desde **Postman** que las citas aparecen en el dashboard de ReflexoPerú.  
- Implementar un **endpoint webhook en Django**:  
  - URL: `/api/webhooks/ghl/appointments/`  
  - Escucha eventos de tipo `AppointmentCreate`.  
  - Guarda la cita entrante en la base de datos o log.  
  - Responde **200 OK** para validar el evento.

---

## 🛠️ Tecnologías utilizadas

- **Django + Django REST Framework** → Backend.  
- **SQLite** → Almacenamiento local.  
- **Requests** → Llamadas a la API de GHL.  
- **Postman** → Pruebas de los endpoints.  
- **GHL API (Calendars)** → Manejo de citas.  

---

## ⚙️ Configuración
- **Python==3.12.10

### 1. Clonar proyecto
```bash
git clone https://github.com/BETO-17/Post-Get-Webhook.git
cd backend
---

##
 
flowchart TD
    A[Cliente / Postman] -->|POST /appointments| B[Django API Backend]
    B -->|Llama API GHL| C[GHL API - Crear cita]
    C -->|Respuesta 201| B
    B -->|Guarda en SQLite| D[(DB Local)]

    E[GHL Dashboard] -->|Webhook AppointmentCreate| F[/api/webhooks/ghl/appointments/]
    F -->|Valida payload + 200 OK| B
    F -->|Guarda log / DB| D

┌───────────────────────────────┐
│ 1. Requisitos                 │
├───────────────────────────────┤
│ - Cuenta GHL activa           │
│ - API Key (Bearer)            │
│ - Django + SQLite             │
│ - Postman / CURL              │
└───────────────────────────────┘

┌───────────────────────────────┐
│ 2. Endpoints GHL              │
├───────────────────────────────┤
│ POST /calendars/events/apmts  │ → Crear cita
│ GET  /calendars/events/apmts  │ → Listar citas
└───────────────────────────────┘

┌───────────────────────────────┐
│ 3. Django – Appointments      │
├───────────────────────────────┤
│ Modelo:                       │
│ • appointmentId               │
│ • calendarId                  │
│ • status                      │
│ • created_at                  │
│                               │
│ Endpoint Webhook:             │
│ • /api/webhooks/ghl/aptms/    │
│ • Valida payload JSON         │
│ • Guarda en log o DB          │
│ • Responde 200 OK             │
└───────────────────────────────┘

┌───────────────────────────────┐
│ 4. Dummy Server (Webhook)     │
├───────────────────────────────┤
│ • Recibe POST de GHL          │
│ • Guarda en webhook.log       │
│ • Imprime en consola          │
└───────────────────────────────┘

┌───────────────────────────────┐
│ 5. Pruebas                    │
├───────────────────────────────┤
│ 1. Crear cita con POST        │
│ 2. Verificar en Dashboard GHL │
│ 3. Recibir Webhook en Django  │
│ 4. Listar citas con GET       │
└───────────────────────────────┘

