from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from users.forms import RegisterForm

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