from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.signout, name='logout'),
    path('bookings/', views.bookings_view, name='bookings'),
    path('book/<int:pk>/', views.book, name='book'),
    path('delete/<int:pk>/', views.delete_booking, name='delete'),
]