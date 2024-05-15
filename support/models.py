from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Support(models.Model):
    who_need_support = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    
    def __str__(self) -> str:
        return self.title
    