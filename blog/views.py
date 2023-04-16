from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, Like, Comment
from django.http import HttpResponse


# Create your views here.
# @login_required(login_url="/account/login/")
def home(request):
    posts = Post.objects.all().order_by('-create_date')
    comments = Comment.objects.all().order_by('-created_date')
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        print(post_id)
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    return render(request, "blog/home.html", {'posts': posts, 'comments': comments})


@login_required(login_url="/account/login/")
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home-page")
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required(login_url="/account/login/")
def create_comment(request, post_id):
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
    like, created = Like.objects.get_or_create(user=user, post_id=post_id)
    if not created:
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    like.save()
    return redirect("home-page")
