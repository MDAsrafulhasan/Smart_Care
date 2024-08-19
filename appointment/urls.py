from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()  # eta router
router.register('', views.AppointmentViewset)  # eta router er antena

urlpatterns = [
    path('', include(router.urls)),
]