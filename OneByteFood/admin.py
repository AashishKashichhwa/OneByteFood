from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'start_time', 'end_time', 'num_people', 'comments', 'payment_option','status')

admin.site.register(Reservation, ReservationAdmin)
