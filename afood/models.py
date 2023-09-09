from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
   date= models.DateField()
   time= models.CharField(max_length=5)
   mb_tables= models.IntegerField(default=1)
   user= models.ForeignKey(User, on_delete=models.CASCADE)
   status= models.CharField(max_length=1, choices=[
    ("P", "pending"),
    ("C", "completed"),
    ("X", "cancelled"),
   ])
