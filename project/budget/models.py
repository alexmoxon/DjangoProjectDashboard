from django.db import models
from django.contrib.auth.models import User



Categories = (
    ('food','Food'),
    ('clothing', 'Clothing'),
    ('housing','Housing'),
    ('education','Education'),
	('entertainment','Entertainment'),
    ('other','Other'),
)

class Budget(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	category = models.CharField(max_length=20, choices=Categories, default='other')
	description= models.CharField(max_length=100)
	projected=models.PositiveIntegerField(default=0)
	actual=models.PositiveIntegerField(default=0)