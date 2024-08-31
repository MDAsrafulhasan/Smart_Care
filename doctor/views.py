from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,filters,pagination
from . models import Doctor,Specialization,Designation,AvailableTime,Review
from . serializers import AvailableTimeSerializer,SpecializationSerializer,DesignationSerializer,DoctorSerializer,ReviewSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1  # items per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
    # filter_backends = [DjangoFilterBackend]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']

class AvailableTimeViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

