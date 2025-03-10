from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any custom fields here if needed
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
