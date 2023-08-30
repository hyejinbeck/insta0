from django.contrib.auth.forms import UserCreationForm , AuthenticationForm 
# AuthenticationForm 추가 
from .models import User 
from django.contrib.auth import get_user_model 

class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model = get_user_model() 
        # model = User 를 대신 사용할 수 있는데 
        # 다만, get_user_model() 쓰는게 유지보수하기 좋다. 
        fields = ('username', 'profile_image',) 
        # profile_image = 사용자가 회원가입할때 프로필사진 올릴수있도록 

class CustomAuthenticationForm(AuthenticationForm): 
    pass 