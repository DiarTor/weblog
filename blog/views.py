from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
# Create your views here.
# @login_required(login_url="/account/login/")
def home(request):
    posts = Post.objects.all().order_by('-create_date')
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        print(post_id)
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    return render(request, "blog/home.html", {'posts':posts})

@login_required(login_url="/account/login/")
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home-page")
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form':form})