from django.db import models

class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    num_people = models.IntegerField()
    comments = models.TextField()
    payment_made = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='pending')

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.CharField(max_length=140, default='1')
    image_url = models.URLField(default='https://example.com/placeholder.jpg')  # Add a default URL
    description = models.TextField(default="No description available")

from django.db import models
from django.contrib.auth.models import User

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-increment primary key field
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        if self.user:
            return f"{self.user.username}'s Cart Item - {self.food_item.name}"
        else:
            return f"Anonymous User's Cart Item - {self.food_item.name}"

class BirthdayThemeReservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    reservation_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    number_of_people = models.IntegerField()
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)



# class Order(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)