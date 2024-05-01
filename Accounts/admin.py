from django.contrib import admin
from .models import UserAddress, UserProfile


admin.site.register(UserProfile)
admin.site.register(UserAddress)

# Register your models here.
