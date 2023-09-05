from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm , CustomAuthenticationForm
from django.contrib.auth import login as auth_login
#from .models import User # 이렇게 직접가져오는것 보다는 유지보수 차원에서 아래 추천 
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request): 
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() 
            return redirect('posts:index')

    else: 
        form = CustomUserCreationForm()  # 모델폼으로 보여주게 해줘(작성할수있도록)

    context = {
        'form': form, 
    }
    return render(request, 'accounts/form.html', context)
    # 아직 form.html 파일을 만들지 않았는데 , 
    # 여기까지 후 작동하게 되면 작성할수있는 어떤 form이 나온다! 
    # 이때 나오는건, posts>templates>forms.html 

def login(request): 
    if request.method == 'POST': 
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid(): 
            user = form.get_user()
            auth_login(request,user)
            return redirect('posts:index')
    else: 
        form = CustomAuthenticationForm() 
    
    context = {
        'form': form, 
    }
    return render(request, 'accounts/form.html', context)

def profile(request, username): 
    User = get_user_model()

    user_info = User.objects.get(username=username)

    context = {
        'user_info': user_info
    }
    return render(request, 'accounts/profile.html', context)

@login_required  # 로그인한사람만 보여지게
def follow(request,username): 
    User = get_user_model()

    me = request.user  # 현재 로그인한사람(나자신)
    # you를 하려면 get_user_model()을 윗칸에다 불러와서 저정해줘야함 
    you = User.objects.get(username=username)
    # 지금 프로필사진 누른 계정 
    
    # 팔로잉이 이미 되어있는 경우 
      # 내가 그 계정의 팔로워들 목록에 있나요? 
      # follower 는 따르는 사람 목록 
      # following 은 따르는 사람 
    if you in me.followings.all(): 
       # if me in you.followers.all() : 와 같다. 
        me.followings.remove(you)
    else: 
        me.followings.add(you)
    return redirect('accounts:profile', username=username)

