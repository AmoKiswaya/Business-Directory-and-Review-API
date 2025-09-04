from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True) 
    is_owner = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True) 

    def __str__(self):
        return self.username 
