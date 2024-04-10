from django.contrib import admin
from django.urls import path, include
from OneByteFood import views as onebytefood_views
from authentication import views as auth_views

urlpatterns = [
    path('', onebytefood_views.index, name='index'),  # Homepage
    path('signup/', auth_views.signup, name='signup'),
    path('signup', auth_views.signup, name='signup'),
    path('activate/<uidb64>/<token>', auth_views.activate, name='activate'),
    path('signin/', auth_views.signin, name='signin'),
    path('signin', auth_views.signin, name='signin'),
    path('signout/', auth_views.signout, name='signout'),
    path('signout', auth_views.signout, name='signout'),
    path('reservation/', onebytefood_views.reservation, name='reservation'),  # Homepage
    path('about/', onebytefood_views.about, name='about'),  # About page
    path('services/', onebytefood_views.services, name='services'),  # Services page
    path('contact/', onebytefood_views.contact, name='contact'),  # Contact page
    path('reserve/', onebytefood_views.reserve_table, name='reserve_table'),
    path('admin_dashboard/', auth_views.admin_dashboard, name='admin_dashboard'),
    # Add other URL patterns as needed
]
