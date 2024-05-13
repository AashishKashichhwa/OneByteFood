from django.contrib import admin
from .models import Reservation
from .models import BirthdayThemeReservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'date', 'start_time', 'end_time', 'num_people', 'comments', 'payment_made','status')

admin.site.register(Reservation, ReservationAdmin)


# from .models import FoodItem

# class Signup_column(admin.ModelAdmin):
#     list_display = ('name', 'price', 'image', 'last_name', 'password', 'admin')

from django.contrib import admin
from .models import FoodItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

@admin.register(BirthdayThemeReservation)
class BirthdayThemeReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'reservation_date', 'start_time', 'end_time', 'number_of_people', 'status']
    search_fields = ['name', 'phone']
    list_filter = ['reservation_date']
    date_hierarchy = 'reservation_date'


