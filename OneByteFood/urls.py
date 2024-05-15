# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),  # Homepage
#     path('reservation/', views.reservation, name='reservation'),
#     path('about/', views.about, name='about'),
#     path('services/', views.services, name='services'),
#     path('contact/', views.contact, name='contact'),
#     # path('reserve/', views.reserve_table, name='reserve_table'),
#     path('reservation_details/', views.reservationDetails, name='reservationDetails'),
#     path('menu/', views.menu_redirect, name='menu_redirect'),
#     path('events/', views.events_redirect, name='events_redirect'),
#     path('gallery/', views.gallery_redirect, name='gallery_redirect'),
#     path('edit_reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
#     path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
# ]


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
from .views import delete_item

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
    path('reservation_details/', onebytefood_views.reservationDetails, name='reservationDetails'),
    path('menu/', onebytefood_views.menu_view, name='menu_redirect'),
    path('events/', onebytefood_views.events_redirect, name='events_redirect'),
    path('gallery/', onebytefood_views.gallery_redirect, name='gallery_redirect'),
    path('admin_dashboard/', auth_views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', auth_views.user_dashboard, name='user_dashboard'),
    path('user_dashboard/menu/', onebytefood_views.menu_view, name='user_menu_redirect'),
    path('user_dashboard/events/', onebytefood_views.events_redirect, name='user_events_redirect'),
    path('user_dashboard/reservation/', onebytefood_views.reservation, name='user_reservation'),
    path('user_dashboard/reservation_details/', onebytefood_views.reservationDetails, name='user_reservationDetails'),
    path('user_dashboard/gallery/', onebytefood_views.gallery_redirect, name='user_gallery_redirect'),
    path('edit_admin/<int:reservation_id>/', onebytefood_views.edit_reservation, name='edit_reservation'),
    path('update_admin/<int:reservation_id>/', onebytefood_views.update_reservation, name='update_reservation'),
    path('delete_admin/<int:reservation_id>/', onebytefood_views.delete_reservation, name='delete_reservation'),
    path('edit_reservation_user/<int:reservation_id>/', onebytefood_views.edit_reservation_user, name='edit_reservation_user'),
    path('update_user/<int:reservation_id>/', onebytefood_views.update_reservation_user, name='update_reservation_user'),
    path('delete_reservation_user/<int:reservation_id>/', onebytefood_views.delete_reservation_user, name='delete_reservation_user'),
    path('reservation/user_reservation_history/', onebytefood_views.user_reservation_history_redirect, name='user_reservation_history_redirect'),
    path('reservation_details/user_reservation_history/', onebytefood_views.user_reservation_history_redirect, name='user_reservation_history_redirect'),
    path('user_reservation_history/', onebytefood_views.show_user_reservation_history, name='show_user_reservation_history'),
    path('cart/', onebytefood_views.cart_view, name='cart_view'),
    path('cart/', onebytefood_views.cart_view, name='cart'),
    path('add_to_cart/', onebytefood_views.add_to_cart, name='add_to_cart'),
    path('events/birthdaytheme', onebytefood_views.birthday, name='Birthday'),
    path('events/unicornR', onebytefood_views.unicornR, name='UnicornR'),
    path('events/events/theme_80', onebytefood_views.theme_80, name='80_theme'),
    path('events/events/babybirthday', onebytefood_views.babybirthday, name='Babybirthday'),
    path('events/reservation', onebytefood_views.reservation, name='Reservation'),
    path('events/user_reservation_history', onebytefood_views.user_reservation_history_redirect, name='user_reservation_history_redirect'),
    path('reservation_theme/', onebytefood_views.reservationTheme, name='reservation_theme'),
    path('reservation_details/',onebytefood_views.reservationDetails, name='reservation_details'),
    path('update_reservation_user/', onebytefood_views.update_reservation_user, name='update_reservation_user'),
    path('cancel_reservation_user/<int:reservation_id>/', onebytefood_views.cancel_reservation_user, name='cancel_reservation_user'),
    path('admin_dashboard/user_details/', onebytefood_views.user_details, name='user_details'),
    path('admin_dashboard/reservation_history/', onebytefood_views.reservation_details, name='reservation_details'),
    path('checkout/', onebytefood_views.checkout, name='checkout'),
    path('delete_item', delete_item, name='delete_item'),
    path('cartcopy/', onebytefood_views.cartcopy, name='cartcopy'),
    path('admin_dashboard/unicorn_reservation_data', onebytefood_views.reservationAdminTheme, name='admin_reservation_details'),
]
