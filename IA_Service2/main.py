from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import predict, symptoms, summary

app = FastAPI(
    title="Health IA Service - Nouhaila",
    description="Service d'intelligence artificielle pour diagnostic médical",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router, prefix="/api/v1", tags=["Prédiction ML"])
app.include_router(symptoms.router, prefix="/api/v1", tags=["Symptômes"])
app.include_router(summary.router, prefix="/api/v1", tags=["Résumé IA"])

from notifications.email_service import (
    send_appointment_reminder,
    send_medication_reminder
)
from pydantic import BaseModel

class AppointmentReminderRequest(BaseModel):
    to_email: str
    patient_name: str
    doctor_name: str
    rdv_time: str

class MedicationReminderRequest(BaseModel):
    to_email: str
    patient_name: str
    medication: str
    dosage: str

@app.post("/api/v1/notify/appointment", tags=["Notifications"])
async def notify_appointment(req: AppointmentReminderRequest):
    result = send_appointment_reminder(
        req.to_email, req.patient_name,
        req.doctor_name, req.rdv_time
    )
    return result

@app.post("/api/v1/notify/medication", tags=["Notifications"])
async def notify_medication(req: MedicationReminderRequest):
    result = send_medication_reminder(
        req.to_email, req.patient_name,
        req.medication, req.dosage
    )
    return result

@app.get("/health")
async def health():
    return {"status": "ok", "service": "ia-service", "version": "1.0.0"}

@app.get("/")
async def root():
    return {"message": "Health IA Service actif", "docs": "/docs"}