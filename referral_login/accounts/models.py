from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    referrer = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='referrals')

    def __str__(self):
        return self.username
