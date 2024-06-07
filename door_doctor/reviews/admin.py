from django.contrib import admin
from .models import Review 

# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'approved', 'created_at', 'token')
    list_filter = ('approved', 'created_at')
    search_fields = ('name', 'street', 'city', 'state', 'zip_code', 'phone_number', 'review_text')