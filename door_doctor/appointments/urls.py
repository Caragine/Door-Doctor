from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('request/', views.request_appointment, name='request_appointment'),
    path('thanks/', views.appointment_thanks, name='appointment_thanks'),
]