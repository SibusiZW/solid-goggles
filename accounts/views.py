from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            password = form.cleaned_data['password']

        userr = authenticate(request, student_id=student_id, password=password)

        if userr:
            login(request, userr)
            return redirect('home')
        else:
            return HttpResponse('Incorrect credentials')
    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })