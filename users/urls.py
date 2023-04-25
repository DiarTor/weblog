from django.urls import path
from users import views
urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('change-username/', views.change_username, name='change_username'),
    path('change-password/', views.CustomPasswordChangeView.as_view(template_name='registration/password-change.html'), name='change_password')
]