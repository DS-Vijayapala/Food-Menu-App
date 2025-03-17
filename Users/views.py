from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    """Register a new user."""

    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
