from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'street', 'city', 'state', 'zip_code', 'phone_number', 'review_text']