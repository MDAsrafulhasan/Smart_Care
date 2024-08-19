from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()  # eta router
router.register('list', views.DoctorViewset)  # eta router er antena
router.register('specialization', views.SpecializationViewset)  # eta router er antena
router.register('available_time', views.AvailableTimeViewset)  # eta router er antena
router.register('designation', views.DesignationViewset)  # eta router er antena
router.register('reviews', views.ReviewViewset)  # eta router er antena

urlpatterns = [
    path('', include(router.urls)),
]