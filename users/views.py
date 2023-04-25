from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.forms import RegisterForm, ChangeUsernameForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


# Create your views here.
class CustomPasswordChangeView(PasswordChangeView):
    from_class = PasswordChangeView
    success_url = reverse_lazy('home-page')
def profile(request):
    return render(request, 'users/profile.html')


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home-page')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def log_in(request):
    return render(request, 'users/templates/registration/login.html')


def change_username(request):
    if request.method == "POST":
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            # if ChangeUsernameForm.check_exist:
            #     messages.error(request, 'Username Is Invalid Please Try Another One.')
            #     form = ChangeUsernameForm()
            # else:
            try:
                user = request.user
                user.username = request.POST['new_username']
                user.save()
                return redirect('home-page')
            except IntegrityError:
                messages.error(request, 'Username Is Invalid Please Try Another One.')
                form = ChangeUsernameForm()
    else:
        form = ChangeUsernameForm()
    return render(request, 'users/change_username.html', {'form': form})
