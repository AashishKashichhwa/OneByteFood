from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'date', 'start_time', 'end_time', 'num_people', 'comments', 'payment_option','status')

admin.site.register(Reservation, ReservationAdmin)


# from .models import FoodItem

# class Signup_column(admin.ModelAdmin):
#     list_display = ('name', 'price', 'image', 'last_name', 'password', 'admin')

from django.contrib import admin
from .models import FoodItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
