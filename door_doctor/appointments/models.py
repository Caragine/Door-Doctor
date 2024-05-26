from django.db import models
from django.utils import timezone

# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=20, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    phone_number = models.CharField(max_length=15)
    reason_for_appointment = models.TextField()
    availability = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name