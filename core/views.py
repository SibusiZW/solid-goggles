from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Consultation, Booking

@login_required(login_url='/auth/login/')
def home(request):
    consultations = Consultation.objects.all()

    return render(request, 'home.html', { 'user': request.user, 'consultations': consultations })

@login_required(login_url='/auth/login/')
def bookings_view(request):
    bookings = Booking.objects.filter(student=request.user)

    return render(request, 'my_bookings.html', { 'bookings': bookings })

@login_required(login_url='/auth/login/')
def signout(request):
    logout(request)
    return redirect('login')