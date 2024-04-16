from django.db import models

# Create your models here.

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    num_people = models.IntegerField()
    comments = models.TextField()
    payment_option = models.CharField(max_length=20)
    status = models.CharField(max_length=50, default='pending')