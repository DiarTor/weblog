from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return HttpResponse("<p> Hi </p>")
def login(request):
    return render(request, 'users/templates/registration/login.html')