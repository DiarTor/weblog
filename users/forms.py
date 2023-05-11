from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class EditProfileForm(forms.Form):
    username_help_text = "Enter Your New Username"
    first_name_help_text = "Enter Your New First Name"
    last_name_help_text = "Enter Your New Last Name"
    email_help_text = "Enter Your New Email"
    username = forms.CharField(max_length=50, help_text=username_help_text, required=False, label="Username :")
    first_name = forms.CharField(max_length=50, help_text=first_name_help_text, required=False, label="First Name :")
    last_name = forms.CharField(max_length=50, help_text=last_name_help_text, required=False, label="Last Name :")
    email = forms.EmailField(max_length=50, help_text=email_help_text, required=False, label="Email :")