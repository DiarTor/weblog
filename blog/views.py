from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required(login_url="/account/login/")
def home(request):
    return render(request, "blog/home.html")

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