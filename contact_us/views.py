from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . models import ContactUs
from . serializers import ContactUsSerializer

class ContactUsViewset(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer