from django.urls import path
from users import views
urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('change-username', views.change_username, name='change_username')
]