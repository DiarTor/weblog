from django.urls import path
from users import views
urlpatters = [
    path('signup/', views.signup, name="signup")
]