from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import HomePage, CreatePost, EditPost, CreateComment

from blog import views

urlpatterns = [
    path('', HomePage.as_view(), name="home-page"),
    path('create-post/', CreatePost.as_view(), name="create_post"),
    path('edit-post/<int:post_id>/', EditPost.as_view(), name="edit_post"),
    path('like-post/', views.like_post, name="like-post"),
    path('like-comment/', views.like_comment, name="like-comment"),
    path('create-comment/<int:post_id>/', CreateComment.as_view(), name='comments')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
