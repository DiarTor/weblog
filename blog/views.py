from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, EditPostForm
from .models import Post, Comment
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
# @login_required(login_url="/account/login/")
def home(request):
    posts = Post.objects.all().order_by('-create_date')
    comments = Comment.objects.all().order_by('-created_date')
    if request.method == "POST":
        try:
            if request.POST['comment-id']:
                comment_id = request.POST.get("comment-id")
                comment = Comment.objects.get(id=comment_id)
                if comment and comment.user == request.user:
                    comment.delete()
        except MultiValueDictKeyError:
            post_id = request.POST.get("post-id")
            print(post_id)
            post = Post.objects.filter(id=post_id).first()
            if post and post.author == request.user:
                post.delete()
    return render(request, "blog/home.html", {'posts': posts, 'comments': comments})

# create a post section
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

# edit post section
def edit_post(request, post_id):
    if request.method == "POST":
        form = EditPostForm(request.POST, request.FILES)
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
        form = EditPostForm()
    return render(request, 'blog/edit_post.html', {"form": form})
# create a comment section
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

# like post section
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
# like comment section
def like_comment(request):
    user = request.user
    if request.method == "POST":
        cmnt_id = request.POST.get('comment_id')
        cmnt = Comment.objects.get(id=cmnt_id)
    if user in cmnt.liked.all():
        cmnt.liked.remove(user)
    else:
        cmnt.liked.add(user)
    return redirect("home-page")


