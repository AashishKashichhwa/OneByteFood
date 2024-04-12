from django.contrib import admin
from .models import Signup_data

class Signup_column(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'password', 'admin')

admin.site.register(Signup_data, Signup_column)
