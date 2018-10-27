from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Reciept(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  email = models.CharField(max_length=100)
  amount = models.IntegerField()
  description = models.TextField()

  
class Transaction(models.Model):
 	# profile = models.ForeignKey(Profile)
 	token = models.CharField(max_length=120)
 	order_id = models.CharField(max_length=120)
 	amount = models.DecimalField(max_digits=100, decimal_places=2)
 	success = models.BooleanField(default=True)
 	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

 	def __str__(self):
 		return self.order_id
 	class Meta:
 		ordering = ['-timestamp']