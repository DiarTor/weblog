from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.forms import RegisterForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})
def login(request):
    return render(request, 'users/templates/registration/login.html')