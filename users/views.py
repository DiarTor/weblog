from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.forms import RegisterForm, ChangeUsernameForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
# Create your views here.
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
    # current_pass = request.user.password
    # print(current_pass, "\n")
    # print(request.POST['password'])
    if request.method == "POST":
        form = ChangeUsernameForm(request.POST)
        if form.is_valid():
            # match_check = check_password(current_pass, request.POST['password'])
            # if match_check:
            #     print('salam')
            owner = request.user
            owner.username = request.POST['new_username']
            owner.save()
    else:
        form = ChangeUsernameForm()
    return render(request, 'users/change_username.html', {'form' : form})