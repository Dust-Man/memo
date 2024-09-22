from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True, null=True)  # Hacerlo opcional temporalmente

    emergency_phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
