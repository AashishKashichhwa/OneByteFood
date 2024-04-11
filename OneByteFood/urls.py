from django.contrib import admin
from django.urls import path, include
from OneByteFood import views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage
    path('reservation/', views.reservation, name='reservation'),  # Homepage
    path('about/', views.about, name='about'),  # About page
    path('services/', views.services, name='services'),  # Services page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('reserve/', views.reserve_table, name='reserve_table'),  # Reserve table view
    # Add other URL patterns as needed
]
