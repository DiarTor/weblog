from django.urls import path
from blog import views
urlpatterns = [
    path('', views.home, name="home-page"),
    path('create-post/', views.create_post, name="create_post")
]