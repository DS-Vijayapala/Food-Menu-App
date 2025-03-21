from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    """Model for user profile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
