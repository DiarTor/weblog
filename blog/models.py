from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
     author = models.ForeignKey(User, on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     content = models.TextField()
     create_date = models.DateTimeField(auto_now_add=True)
     edited_date = models.DateTimeField(auto_now=True)
     image = models.ImageField(upload_to='images/')

     def __str__(self):
        return self.title + "\n" +self.content