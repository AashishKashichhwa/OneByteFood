# from django.contrib import admin
# from django.urls import path, include
# from OneByteFood import views as onebytefood_views
# from authentication import views as auth_views

# urlpatterns = [
#     path('', onebytefood_views.index, name='index'), # Homepage
#     path('signup/', auth_views.signup, name='signup'),
#     path('signup', auth_views.signup, name='signup'),
#     path('signin/', auth_views.signin, name='signin'),
#     path('signin', auth_views.signin, name='signin'),
#     path('activate/<uidb64>/<token>', auth_views.activate, name='activate'),
#     path('authentication/signin/', auth_views.signin, name='signin'),
#     path('signout', auth_views.signout, name='signout'),
#     # path('reservation/', onebytefood_views.reservation, name='reservation'),  # Homepage
#     # path('reservation/', onebytefood_views.reserve_table, name='reserve_table'),  # Homepage
#     path('reservation/', onebytefood_views.reservation, name='reservation'),
#     path('reservation_details/', onebytefood_views.reservation_history, name='reservation_history'),  # Reserve table view
#     # path('about/', onebytefood_views.about, name='about'),  # About page
#     # path('services/', onebytefood_views.services, name='services'),  # Services page
#     # path('contact/', onebytefood_views.contact, name='contact'),  # Contact page
#     path('menu/', onebytefood_views.menu_redirect, name='menu_redirect'),
#     path('events/', onebytefood_views.events_redirect, name='events_redirect'),
#     path('gallery/', onebytefood_views.gallery_redirect, name='gallery_redirect'),
#     path('admin_dashboard/', auth_views.admin_dashboard, name='admin_dashboard'),
#     path('user_dashboard/', auth_views.user_dashboard, name='user_dashboard'),
#     path('user_dashboard/menu/', onebytefood_views.menu_redirect, name='menu_redirect'),
#     path('user_dashboard/events/', onebytefood_views.events_redirect, name='events_redirect'),
#     path('user_dashboard/reservation/', onebytefood_views.reservation, name='reservation'),
#     path('user_dashboard/reservation_details/', onebytefood_views.reservation_history, name='reservation_history'),  # Reserve table view
#     path('user_dashboard/gallery/', onebytefood_views.gallery_redirect, name='gallery_redirect'),
#     # path('gallery/menu/', onebytefood_views.menu_redirect, name='gallery_menu_redirect'),
#     path('gallery/events/', onebytefood_views.events_redirect, name='events_redirect'),
#     path('gallery/reservation/', onebytefood_views.reservation, name='reservation'),
#     path('gallery/reservation_details/', onebytefood_views.reservation_history, name='reservation_history'),  # Reserve table view
#     path('gallery/gallery/', onebytefood_views.gallery_redirect, name='gallery_redirect'),
# ]

from django.urls import path
from OneByteFood import views as onebytefood_views
from authentication import views as auth_views

urlpatterns = [
    path('', onebytefood_views.index, name='index'),  # Homepage
    path('signup/', auth_views.signup, name='signup'),
    path('signup', auth_views.signup, name='signup'),
    path('signin/', auth_views.signin, name='signin'),
    path('signin', auth_views.signin, name='signin'),
    path('authentication/signin', auth_views.signin, name='signin'),
    path('authentication/signin/', auth_views.signin, name='signin'),
    path('activate/<uidb64>/<token>/', auth_views.activate, name='activate'),
    path('signout/', auth_views.signout, name='signout'),
    path('reservation/', onebytefood_views.reservation, name='reservation'),
    path('reservation_details/', onebytefood_views.reservation_history, name='reservation_history'),
    path('menu/', onebytefood_views.menu_redirect, name='menu_redirect'),
    path('events/', onebytefood_views.events_redirect, name='events_redirect'),
    path('gallery/', onebytefood_views.gallery_redirect, name='gallery_redirect'),
    path('admin_dashboard/', auth_views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', auth_views.user_dashboard, name='user_dashboard'),
    path('user_dashboard/menu/', onebytefood_views.menu_redirect, name='user_menu_redirect'),
    path('user_dashboard/events/', onebytefood_views.events_redirect, name='user_events_redirect'),
    path('user_dashboard/reservation/', onebytefood_views.reservation, name='user_reservation'),
    path('user_dashboard/reservation_details/', onebytefood_views.reservation_history, name='user_reservation_history'),
    path('user_dashboard/gallery/', onebytefood_views.gallery_redirect, name='user_gallery_redirect'),
    path('gallery/menu/', onebytefood_views.menu_redirect, name='gallery_menu_redirect'),
    path('gallery/events/', onebytefood_views.events_redirect, name='gallery_events_redirect'),
    path('gallery/reservation/', onebytefood_views.reservation, name='gallery_reservation'),
    path('gallery/reservation_details/', onebytefood_views.reservation_history, name='gallery_reservation_history'),
    path('gallery/home/', onebytefood_views.index, name='gallery_home_redirect'),  # Redirect to index from gallery
    path('edit/<int:reservation_id>/', onebytefood_views.edit_reservation, name='edit_reservation'),
    path('update/<int:reservation_id>/', onebytefood_views.update_reservation, name='update_reservation'),
    path('delete/<int:reservation_id>/', onebytefood_views.delete_reservation, name='delete_reservation'),
]
