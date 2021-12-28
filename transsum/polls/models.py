from django.db import models

# Create your models here.
class Summary(models.Model):
    video_link = models.CharField(max_length=50)
    summary = models.CharField(max_length=2000)

    def __str__(self):
        return self.video_link
