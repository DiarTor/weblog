from django.urls import path
from auth1 import views
urlpatterns = [
    path("signup/" , views.signup , name="sign-up")
]