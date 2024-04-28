from django.contrib.auth.models import User
from django.db import models
from .constants import BLOOD_GROUP, GENDER,DISTRICT_CHOICES
from datetime import date
from django.apps import apps


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER)
    image = models.ImageField(upload_to='Accounts/images/', null=True, blank=True)
    last_donation_date = models.DateField(null=True, blank=True)
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Weight in kilograms

    def calculate_age(self):
        today = date.today()
        if self.birth_date is not None:
            return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return None

    def calculate_bmi(self):
     if self.height and self.weight:
        try:
            height_in_meters = float(self.height) * 0.3048  # Convert height from feet to meters as float
            weight_in_kg = float(self.weight)
            return weight_in_kg / (height_in_meters ** 2)
        except ValueError:
            return None
     return None
    
    def has_pending_requests(self):
        BloodRequest = apps.get_model('donationcenters', 'BloodRequest')
        return BloodRequest.objects.filter(requester=self.user, is_fulfilled=False).exists()

    
    

    def __str__(self):
        return f'Profile of {self.user.username}'


class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    street_address = models.CharField(max_length=40)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=40)

    def __str__(self):
        return f'Address of {self.user.username}'

