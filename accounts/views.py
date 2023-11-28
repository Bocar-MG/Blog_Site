from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import CustomUserRegistrationForm


# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('blog:dashboard'))

    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('blog:dashboard'))
    else:
        form = CustomUserRegistrationForm()
    render(request, 'accounts/register.html', {'form': form})
