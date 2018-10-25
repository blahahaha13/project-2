from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reciept(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  email = models.CharField(max_length=100)
  amount = models.IntegerField()
  description = models.TextField()

