from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from .constants import BLOOD_GROUP,BLOOD_NEED,blood_bag_quantity,blood_hemoglobin_levels
from django.utils import timezone

class BLoodRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=200, choices=BLOOD_GROUP, null=True)
    why_need = models.CharField(max_length=200, choices=BLOOD_NEED, null=True)
    where_need = models.CharField(max_length=200, null=True)
    donation_date = models.DateTimeField(null=True)
    blood_quantity = models.CharField(max_length=200, choices=blood_bag_quantity, null=True)
    hemoglobin_level = models.CharField(max_length=10, choices=blood_hemoglobin_levels, null=True)
    hospital_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    additional_information = models.TextField(null=True)
    is_donate = models.BooleanField(default=False,null=True) 
    created_at = models.DateTimeField(auto_now_add=True,null=True)  

    def __str__(self):
        return f"Requester is {self.requester}"



class EmergencyBloodRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=200, choices=BLOOD_GROUP, null=True)
    why_need = models.CharField(max_length=200, choices=BLOOD_NEED, null=True)
    where_need = models.CharField(max_length=200, null=True)
    donation_date = models.DateTimeField(null=True)
    blood_quantity = models.CharField(max_length=200, choices=blood_bag_quantity, null=True)
    hemoglobin_level = models.CharField(max_length=10, choices=blood_hemoglobin_levels, null=True)
    hospital_name = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    additional_information = models.TextField(null=True)
    is_donate = models.BooleanField(default=False,null=True) 
    created_at = models.DateTimeField(auto_now_add=True,null=True)  

    def __str__(self):
        return f"Requester is {self.requester}"
    

# ......