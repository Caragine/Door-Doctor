from django import forms
from django.core.exceptions import ValidationError
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'street', 'city', 'zip_code', 'phone_number', 'review_text']
        widgets = {'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Name'}), 
                   'street': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Address'}), 
                   'city': forms.TextInput(attrs={'class': "form-control", 'placeholder': 'City'}), 
                   'zip_code': forms.TextInput(attrs={'class': "form-control", 'placeholder': '#####'}), 
                   'phone_number': forms.TextInput(attrs={'class': "form-control", 'placeholder': '##########'}),
                   'review_text': forms.Textarea(attrs={'class': "form-control"})}

    def clean(self):
        form_data = self.cleaned_data
        if len(form_data['phone_number']) != 10:
            raise ValidationError("Please enter a 10 digit phone number without spaces or symbols")
        if len(form_data['zip_code']) != 5:
            raise ValidationError("Please enter a valid 5 digit zip code")
        form_data['city'] = form_data['city'].title()
        form_data['name'] = form_data['name'].title()
        form_data['street'] = form_data['street'].title()

        return form_data
