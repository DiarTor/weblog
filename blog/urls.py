from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name="home-page"),
    path('create-post/', views.create_post, name="create_post"),
    path('like/', views.like_post, name="like-post"),
    path('<int:post_id>/comments/', views.comments, name='comments')
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)