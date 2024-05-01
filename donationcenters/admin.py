from django.contrib import admin
from .models import BLoodRequest,EmergencyBloodRequest

# Register your models here....
admin.site.register(BLoodRequest)
admin.site.register(EmergencyBloodRequest)
