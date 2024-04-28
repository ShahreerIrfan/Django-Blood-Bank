from django import forms
from .models import BLoodRequest

from django import forms
from .models import BLoodRequest,EmergencyBloodRequest

class BLoodRequestForm(forms.ModelForm):
    class Meta:
        model = BLoodRequest
        exclude = ['requester', 'is_donate']
        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-input'}),
            'why_need': forms.Select(attrs={'class': 'form-input'}),
            'where_need': forms.TextInput(attrs={'class': 'form-input'}),
            'donation_date': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'blood_quantity': forms.Select(attrs={'class': 'form-input'}),
            'hemoglobin_level': forms.Select(attrs={'class': 'form-input'}),
            'hospital_name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
            'additional_information': forms.Textarea(attrs={'class': 'form-textarea'}),
        }

    def __init__(self, *args, **kwargs):
        super(BLoodRequestForm, self).__init__(*args, **kwargs)
        self.fields['donation_date'].input_formats = ['%Y-%m-%dT%H:%M']

class EmergencyBLoodRequestForm(forms.ModelForm):
    class Meta:
        model = EmergencyBloodRequest
        exclude = ['requester', 'is_donate']
        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-input'}),
            'why_need': forms.Select(attrs={'class': 'form-input'}),
            'where_need': forms.TextInput(attrs={'class': 'form-input'}),
            'donation_date': forms.DateTimeInput(attrs={'class': 'form-input', 'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'blood_quantity': forms.Select(attrs={'class': 'form-input'}),
            'hemoglobin_level': forms.Select(attrs={'class': 'form-input'}),
            'hospital_name': forms.TextInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
            'additional_information': forms.Textarea(attrs={'class': 'form-textarea'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmergencyBLoodRequestForm, self).__init__(*args, **kwargs)
        self.fields['donation_date'].input_formats = ['%Y-%m-%dT%H:%M']