from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.views import View

from .forms import PostForm, CommentForm, EditPostForm
from .models import Post, Comment


# Create your views here.
class HomePage(View):
    template_name = 'blog/home.html'

    def get_posts_and_comments(self):
        posts = Post.objects.all().order_by('-create_date')
        comments = Comment.objects.all().order_by('-created_date')
        return posts, comments

    def get(self, request):
        posts, comments = self.get_posts_and_comments()
        return render(request, self.template_name, {'posts': posts, 'comments': comments})

    def post(self, request):
        posts, comments = self.get_posts_and_comments()

        if request.method == "POST":
            try:
                if request.POST['comment-id']:
                    comment_id = request.POST.get("comment-id")
                    comment = Comment.objects.get(id=comment_id)
                    if comment and comment.user == request.user:
                        comment.delete()
                        # Update comments after deleting a comment
                        comments = Comment.objects.all().order_by('-created_date')
            except MultiValueDictKeyError:
                post_id = request.POST.get("post-id")
                post = Post.objects.filter(id=post_id).first()
                if post and post.author == request.user:
                    post.delete()
                    # Update posts after deleting a post
                    posts = Post.objects.all().order_by('-create_date')

        return render(request, self.template_name, {'posts': posts, 'comments': comments})



#@login_required(login_url="/account/login/")
class CreatePost(View):
    template_name = "blog/create_post.html"
    form_class = PostForm
    success_url = reverse_lazy('home-page')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == "POST":
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect(self.success_url)
        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})


class EditPost(View):
    template_name = "blog/edit_post.html"
    form_class = EditPostForm
    def get(self, request, post_id):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, post_id):
        if request.method == "POST":
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                post = Post.objects.get(id=post_id)
                if not request.POST['title'] == '':
                    post.title = request.POST['title']
                if not request.POST['content'] == '':
                    post.content = request.POST['content']
                try:
                    if not request.FILES['image'] == '':
                        post.image = request.FILES['image']
                except MultiValueDictKeyError:
                    pass
                post.author = request.user
                post.save()
                return redirect('home-page')
        else:
            form = self.form_class()
        return render(request, self.template_name, {'form': form})

class CreateComment(View):
    template_name = "blog/comment.html"
    form_class = CommentForm

    def get(self, request, post_id):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request, post_id):
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post_id = post_id
                comment.user_id = request.user.id
                comment.save()
                return redirect("home-page")
        else:
            form = CommentForm()
        return render(request, 'blog/comment.html', {"form": form})


def like_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = Post.objects.get(id=post_id)
    if user in post.liked.all():
        post.liked.remove(user)
    else:
        post.liked.add(user)
    return redirect("home-page")


def like_comment(request):
    user = request.user
    if request.method == "POST":
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(id=comment_id)
    if user in comment.liked.all():
        comment.liked.remove(user)
    else:
        comment.liked.add(user)
    return redirect("home-page")
