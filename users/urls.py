from django.urls import path

from . import views
from .views import UserProfile, EditProfile, SignUp

urlpatterns = [
    path('profile/', UserProfile.as_view(), name="profile"),
    path('sign-up/', SignUp.as_view(), name='sign_up'),
    path('edit-profile/', EditProfile.as_view(), name='edit_profile'),
    path('change-password/', views.CustomPasswordChangeView.as_view(template_name='registration/password-change.html'),
         name='change_password')
]
