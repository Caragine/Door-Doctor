from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'street', 'city', 'state', 'zip_code', 'phone_number', 'reason_for_appointment', 'availability']