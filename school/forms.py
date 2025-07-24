# shop/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Talaba ID')
    password = forms.CharField(widget=forms.PasswordInput)
