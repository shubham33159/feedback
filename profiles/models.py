from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # image = models.FileField(upload_to="image")
    image = models.ImageField(upload_to="image")