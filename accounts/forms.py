from django import forms

class LoginForm(forms.Form):
    student_id = forms.CharField(max_length=10, widget=forms.TextInput(attrs={ 'placeholder': "Enter student ID", 'class': 'w-[90%] mb-4 p-2 border border-orange-500 rounded-md' }))
    password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={ 'placeholder': "Enter password", 'class': 'w-[90%] mb-4 p-2 border border-orange-500 rounded-md' }))