from django.shortcuts import render, redirect # redirect추가 
from .models import Post
from .forms import PostForm, CommentForm #모델폼 만든거 추가 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


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

@login_required
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

@login_required
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

@login_required # 로그인해야만 작동 
def like(request, post_id): 

    # 좋아요 버튼을 누른 유저 
    user = request.user 
    post = Post.objects.get(id=post_id)

    # 좋아요 버튼을 누른경우, 
    # 이 유저가, 좋아요누른사람들 목록에 있나요? 
    if post in user.like_posts.all(): 
        post.like_users.remove(user)
        # user.like_posts.remove(post)와 같다. 
        # 그리고 한번 누르면 지워져야함
    
    # 좋아요 버튼을 아직 안누른 경우, 
    else: 
        post.like_users.add(user)
        # user.like_posts.add(post)와 같다. 

    return redirect('posts:index')

def like_async(request, post_id): 
    # context = {
    #     'message': post_id, 
    # }
    user = request.user
    post = Post.objects.get(id=post_id)

    if user in post.like_users.all(): 
        post.like_users.remove(user)
        status = False 
    else: 
        post.like_users.add(user)
        status = True 
    
    context = {
        'status': status,
        'count': len(post.like_users.all())
    }

    return JsonResponse(context)
    # 이건 데이터 그 자체를 return 해줌 
    # html 문서를 return 할 필요가 없음 

def delete(request,post_id): 
    post = Post.objects.get(id=post_id)

    post.delete()

    return redirect('posts:index')

def update(request,post_id): 
    post = Post.objects.get(id=post_id)

    if request.method == 'POST': 
        pass 
    else: 
        form = PostForm(instance=post)

    context = {
        'form': form, 
    }
    return render(request, 'update.html', context)