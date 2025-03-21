""" Views for the Users app. """

from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import RegisterForm
from django.contrib.auth.decorators import login_required

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


@login_required
def profilepage(request):
    """ Profile page for the user."""

    return render(request, 'users/profile.html')
