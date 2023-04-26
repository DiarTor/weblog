from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home-page"),
    path('create-post/', views.create_post, name="create_post"),
    path('edit-post/<int:post_id>/', views.edit_post, name="edit_post"),
    path('like-post/', views.like_post, name="like-post"),
    path('like-comment/', views.like_comment, name="like-comment"),
    path('create-comment/<int:post_id>/', views.create_comment, name='comments')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
