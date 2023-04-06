from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate

# Create your views here.
def signup(request):
    return render(request, "auth1/signup.html" ,)