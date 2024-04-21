from django import forms
from .models import BloodRequest

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['reason', 'location', 'needed_by']
        widgets = {
            'needed_by': forms.DateInput(attrs={'type': 'date'})
        }
