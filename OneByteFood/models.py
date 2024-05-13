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