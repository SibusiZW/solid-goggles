from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.signout, name='logout'),
    path('bookings/', views.bookings_view, name='bookings')
]