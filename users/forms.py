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


class ChangeUsernameForm(forms.Form):
    username_help_text = "Enter Your New Username"
    username = forms.CharField(max_length=50, help_text=username_help_text, required=False)

    @property
    def check_exist(self):
        if User.objects.filter(username=self.new_username).exists():
            return True
