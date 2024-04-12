from django.contrib import admin
from django.urls import path, include
from OneByteFood import views as onebytefood_views
from authentication import views as auth_views

urlpatterns = [
    path('', onebytefood_views.index, name='index'), # Homepage
    path('signup/', auth_views.signup, name='signup'),
    path('signup', auth_views.signup, name='signup'),
    path('signin/', auth_views.signin, name='signin'),
    path('signin', auth_views.signin, name='signin'),
    path('activate/<uidb64>/<token>', auth_views.activate, name='activate'),
    path('authentication/signin/', auth_views.signin, name='signin'),
    path('signout', auth_views.signout, name='signout'),
    path('reservation/', onebytefood_views.reservation, name='reservation'),  # Homepage
    # path('reservation/', onebytefood_views.reserve_table, name='reserve_table'),  # Homepage
    path('reservation_details/', onebytefood_views.reserve_table, name='reserve_table'),  # Reserve table view
    path('1/', onebytefood_views.reservation_history, name='reservation_history'),
    path('about/', onebytefood_views.about, name='about'),  # About page
    path('services/', onebytefood_views.services, name='services'),  # Services page
    path('contact/', onebytefood_views.contact, name='contact'),  # Contact page
    path('menu/', onebytefood_views.menu_redirect, name='menu_redirect'),
    path('events/', onebytefood_views.events_redirect, name='events_redirect'),
    path('gallery/', onebytefood_views.gallery_redirect, name='gallery_redirect'),
    path('admin_dashboard/', auth_views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', auth_views.user_dashboard, name='user_dashboard'),
    path('edit/<int:reservation_id>/', onebytefood_views.edit_reservation, name='edit_reservation'),
    path('update/<int:reservation_id>/', onebytefood_views.update_reservation, name='update_reservation'),
    path('delete/<int:reservation_id>/', onebytefood_views.delete_reservation, name='delete_reservation'),
]
