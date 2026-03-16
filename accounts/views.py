from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request)

        student_id = form.cleaned_data['student_id']
        password = form.cleaned_data['password']
    else:
        form = LoginForm()

    return render(request, 'login.html', { 'form': form })