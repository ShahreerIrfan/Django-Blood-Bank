from django.db import models
from django.conf import settings

class BloodRequest(models.Model):
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blood_requests')
    reason = models.TextField()
    location = models.CharField(max_length=255)
    needed_by = models.DateField()
    is_fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return f'Blood Request by {self.requester.username} for {self.needed_by}'

