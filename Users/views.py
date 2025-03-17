""" Views for the Users app. """

from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import RegisterForm

# Create register view


def register(request):
    """Register a new user."""

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Welcome {username}! Your account has been created.')
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)
