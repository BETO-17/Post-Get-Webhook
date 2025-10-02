from django.urls import path

from .views import (
    AppointmentCreateView,appointment_webhook
)

urlpatterns = [
    path('create/', AppointmentCreateView.as_view(), name="create_appointment"),
    path("webhooks/appointments/", appointment_webhook, name="appointment_webhook"),
]