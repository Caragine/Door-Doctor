from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'reason_for_appointment', 'availability', 'street', 'city', 'state', 'zip_code')
