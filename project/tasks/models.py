from django.db import models
from django.contrib.auth.models import User

Categories = (
    ('home', 'Home'),
    ('school', 'School'),
    ('work', 'Work'),
    ('self-improvement', 'Self-improvement'),
    ('other', 'Other'),
)

COMPLETED = (
    ('Yes', 'Yes'),
    ('No', 'No')
)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=20, choices=Categories, default='other')
    description = models.CharField(max_length=100)
    is_completed = models.BooleanField(choices=COMPLETED, default="No")
