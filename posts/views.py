from django.shortcuts import render, redirect # redirect추가 
from .models import Post
from .forms import PostForm, CommentForm #모델폼 만든거 추가 

# Create your views here.

def index(request): 
    # posts = Post.objects.all() 
    # 모든 값을 보여줘 
    posts = Post.objects.all().order_by('-id')
    # id값(작성순서)를 역순으로 보여줘
    # 최신작성된 거 먼저 보여줘
    comment_form = CommentForm()

    context = {
        'posts' : posts, 
        'comment_form' : comment_form,
    }

    return render(request, 'index.html', context)

def create(request): 
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            post.user = request.user
            post.save() 
            return redirect('posts:index')
    else: 
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request,'form.html',context)

def comment_create(request, post_id): 
    comment_form = CommentForm(request.POST) 
    # 작성자가 댓글칸에 입력값(request.POST)을 CommentForm빈 폼에 기재한 것을 
    # comment_form이라고 한다. 

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # commit 은 데이터베이스에 저장하는 단위중 하나 
        # commit=False는 저장하기전까지만 해! 

        # comment에는 로그인유저 (댓글작성자) 와 작성한내용이 담긴다. 
        comment.user = request.user 
        # 그리고 그 유저가 작성한 내용 
        post = Post.objects.get(id=post_id)
        comment.post = post

        comment.save()
        return redirect('posts:index')

        # 이제 로그인된 상황에서 댓글작성해보자