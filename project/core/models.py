from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tasks_view_hide_completed = models.BooleanField(default=False)

def __str__(self):
    return self.user.username