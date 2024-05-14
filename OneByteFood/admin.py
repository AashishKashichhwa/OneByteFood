from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'date', 'start_time', 'end_time', 'num_people', 'comments', 'payment_made','status')

admin.site.register(Reservation, ReservationAdmin)


# from .models import FoodItem

# class Signup_column(admin.ModelAdmin):
#     list_display = ('name', 'price', 'image', 'last_name', 'password', 'admin')

from django.contrib import admin
from .models import FoodItem, CartItem

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_food_name', 'user', 'quantity', 'price')  # Display food name, user, name, and quantity

    def get_food_name(self, obj):
        return obj.food_item.name
    
    get_food_name.short_description = 'Food Name'


from OneByteFood.models import birthday_theme_reservation
class birthdayThemeReservationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'date', 'start_time', 'end_time', 'num_people', 'comments', 'payment_made','status','theme')
    # search_fields = ['name', 'phone']
    # list_filter = ['reservation_date']
    # date_hierarchy = 'reservation_date'

admin.site.register(birthday_theme_reservation, birthdayThemeReservationAdmin)
