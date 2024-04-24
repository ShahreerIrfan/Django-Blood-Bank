from django import forms
from .models import BLoodRequest

from django import forms
from .models import BLoodRequest

class BLoodRequestForm(forms.ModelForm):
    class Meta:
        model = BLoodRequest
        exclude = ['requester', 'is_donate']  
        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-input'}),
            'why_need': forms.Select(attrs={'class': 'form-input'}),
            'where_need': forms.TextInput(attrs={'class': 'form-input'}),
            'donation_date': forms.DateTimeInput(attrs={'class': 'form-input'}),
            'blood_quantity': forms.Select(attrs={'class': 'form-input'}),
            'hemoglobin_level': forms.Select(attrs={'class': 'form-input'}),
            'hospital_name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
            'additional_information': forms.Textarea(attrs={'class': 'form-textarea'}),
        }
