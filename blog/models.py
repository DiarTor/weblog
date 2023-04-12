from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', default=None)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.like.all().count()


like_choices = (
    ("Like", "like"),
    ("Unlike", "Unlike"),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=like_choices, default='like', max_length=10)

    def __str__(self):
        return str(self.post)
