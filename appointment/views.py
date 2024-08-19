from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from . models import Appointment
from . serializers import AppointmentSerializer

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    # custom query kortesi
    def get_queryset(self):
        queryset = super().get_queryset() # parent ke inherit korlam (mane 10 number line ke ekhane anlam)
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
        