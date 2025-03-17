""" Forms for the Users app."""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    """ Form for registering a new user."""
    email = forms.EmailField()

    class Meta:
        """ Meta class for the form."""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
