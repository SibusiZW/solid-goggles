from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.db import IntegrityError
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

@login_required(login_url='/auth/login/')
def book(request, pk):
    try:
        c = get_object_or_404(Consultation, pk=pk)
        obj = Booking.objects.create(consultation=c, student=request.user)
        obj.save()

        return redirect('home')
    except IntegrityError:
        return HttpResponse("You've already booked!")

@login_required(login_url='/auth/login/')
def delete_booking(request, pk):
    obj = get_object_or_404(Booking, pk=pk)
    obj.delete()
    return redirect('home')