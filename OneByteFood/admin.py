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
    list_display = ('id', 'get_image_url', 'get_food_name', 'user', 'quantity', 'price')  # Display food name, user, name, and quantity

    def get_image_url(self, obj):
        return obj.food_item.image_url
    
    def get_food_name(self, obj):
        return obj.food_item.name
    
    get_image_url.short_description = 'Image URL'
    get_food_name.short_description = 'Food Name'


from OneByteFood.models import birthday_theme_reservation
class birthdayThemeReservationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'phone', 'date', 'start_time', 'end_time', 'num_people', 'comments', 'payment_made','status','theme')
    # search_fields = ['name', 'phone']
    # list_filter = ['reservation_date']
    # date_hierarchy = 'reservation_date'

admin.site.register(birthday_theme_reservation, birthdayThemeReservationAdmin)

from django.contrib import admin
from .models import Order, Item

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'place', 'phone', 'total_items', 'total_price')
    list_filter = ('name', 'place', 'phone')
    search_fields = ('name', 'place', 'phone')
    readonly_fields = ('total_items', 'total_price')  # These fields are read-only in admin panel

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'name', 'price', 'quantity')
    list_filter = ('order', 'name')
    search_fields = ('name',)
