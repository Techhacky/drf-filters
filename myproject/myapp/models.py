from django.db import models

# Create your models here.
from django.db import models

# Introduction model
class Introduction(models.Model):
    name = models.CharField(max_length=100)
    intro = models.CharField(max_length=1000, blank=True)
    video_link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name