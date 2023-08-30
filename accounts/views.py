from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm , CustomAuthenticationForm
from django.contrib.auth import login as auth_login
#from .models import User # 이렇게 직접가져오는것 보다는 유지보수 차원에서 아래 추천 
from django.contrib.auth import get_user_model

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