from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from users.forms import RegisterForm, EditProfileForm


# Create your views here.
class CustomPasswordChangeView(PasswordChangeView):
    from_class = PasswordChangeView
    success_url = reverse_lazy('home-page')


class UserProfile(View):
    def get(self, request):
        return render(request, "users/profile.html")


class EditProfile(View):
    def get(self, request):
        form = EditProfileForm()
        return render(request, 'users/edit_profile.html', {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = EditProfileForm(request.POST)
            if form.is_valid():
                # Change Username
                if not request.POST['username'] == '':
                    try:
                        user_username = request.user
                        user_username.username = request.POST['username']
                        user_username.save()
                        return redirect('edit_profile')
                    except IntegrityError:
                        messages.error(request, 'Username Is Invalid Please Try Another One.')
                        form = EditProfileForm()
                # Change First Name
                if not request.POST['first_name'] == '':
                    user_first_name = User.objects.get(id=request.user.id)
                    user_first_name.first_name = request.POST['first_name']
                    user_first_name.save()
                    return redirect('edit_profile')
                # Change Last Name
                if not request.POST['last_name'] == '':
                    user_last_name = User.objects.get(id=request.user.id)
                    user_last_name.last_name = request.POST['last_name']
                    user_last_name.save()
                    return redirect('edit_profile')
                # Change Email
                if not request.POST['email'] == '':
                    user_email = User.objects.get(id=request.user.id)
                    user_email.email = request.POST['email']
                    user_email.save()
                    return redirect('edit_profile')
        else:
            form = EditProfileForm()
        return render(request, 'users/edit_profile.html', {'form': form})


class SignUp(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/sign_up.html', {'form': form})

    def post(self, request):
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
