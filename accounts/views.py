from django.shortcuts import render
from .forms import CustomUserCreationForm # 모델폼 추가 

# Create your views here.

def signup(request): 
    if request.method == 'POSt': 
        pass
    else: 
        form = CustomUserCreationForm()  # 모델폼으로 보여주게 해줘(작성할수있도록)

    context = {
        'form': form, 
    }
    return render(request, 'accounts/form.html', context)
    # 아직 form.html 파일을 만들지 않았는데 , 
    # 여기까지 후 작동하게 되면 작성할수있는 어떤 form이 나온다! 
    # 이때 나오는건, posts>templates>forms.html 