from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserAddress
from .constants import BLOOD_GROUP, GENDER,DISTRICT_CHOICES

class UserProfileForm(forms.ModelForm):
    # Fields from User model
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=False)

    # Fields from UserProfile model
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER)
    phone_number = forms.CharField(max_length=15, required=False)
    image = forms.ImageField(required=False)
    last_donation_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    district = forms.ChoiceField(choices=DISTRICT_CHOICES)
    height = forms.CharField(max_length=10, required=False)
    weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False)

    # Fields from UserAddress model
    street_address = forms.CharField(max_length=40, required=False)
    postal_code = forms.IntegerField(required=False)
    country = forms.CharField(max_length=40, required=False)

    class Meta:
        model = User
        fields = [
            'username', 'password', 'first_name', 'last_name', 'email', 
            'blood_group', 'birth_date', 'gender', 'phone_number', 'image', 
            'last_donation_date', 'district', 'height', 'weight',
            'street_address', 'postal_code', 'country'
        ]

    def save(self, commit=True):
        user_data = {
            'username': self.cleaned_data['username'],
            'first_name': self.cleaned_data['first_name'],
            'last_name': self.cleaned_data['last_name'],
            'email': self.cleaned_data['email']
        }
        user = User(**user_data)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                blood_group=self.cleaned_data.get('blood_group'),
                birth_date=self.cleaned_data.get('birth_date'),
                gender=self.cleaned_data.get('gender'),
                phone_number=self.cleaned_data.get('phone_number'),
                image=self.cleaned_data.get('image'),
                last_donation_date=self.cleaned_data.get('last_donation_date'),
                district=self.cleaned_data.get('district'),
                height=self.cleaned_data.get('height'),
                weight=self.cleaned_data.get('weight')
            )
            UserAddress.objects.create(
                user=user,
                street_address=self.cleaned_data.get('street_address'),
                postal_code=self.cleaned_data.get('postal_code'),
                country=self.cleaned_data.get('country')
            )
        return user



class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

