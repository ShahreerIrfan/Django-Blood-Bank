from django.db import models

# Create your models here.
class VlogPost(models.Model):
    vlog_title = models.CharField(max_length=400)
    vlog_descrription = models.TextField()
    vlog_image = models.ImageField(upload_to="vlog/images")
    vlog_post_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.vlog_title}"
    