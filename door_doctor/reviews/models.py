from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=2, default='NY')
    zip_code = models.CharField(max_length=10, null=True, verbose_name='Zip Code')
    phone_number = models.CharField(max_length=15, null=True, verbose_name='Phone Number')
    review_text = models.TextField(verbose_name='Review')
    created_at = models.DateTimeField(default=timezone.now())
    approved = models.BooleanField(default=False)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name
