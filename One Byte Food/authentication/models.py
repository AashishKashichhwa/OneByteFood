from django.db import models

class Signup_data(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)  # Add a password field to store the password

    def __str__(self):
        return self.username
