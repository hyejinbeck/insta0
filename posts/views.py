from django.shortcuts import render, redirect # redirect추가 
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request): 
    posts = Post.objects.all()

    context = {
        'posts' : posts, 
    }

    return render(request, 'index.html', context)

def create(request): 
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES)
        # request.POST 사용자가 입력한 사진 
        # request.FILES 그 사진을 파일화 함 
        if form.is_valid(): 
            form.save() 
            return redirect('posts:index')
    else: 
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request,'form.html',context)