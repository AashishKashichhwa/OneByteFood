from django.db import models

# Create your models here.
class Signup_data(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    admin = models.BooleanField(default=False)  # New field for Admin
    
    def __str__(self):
        return self.username
