from django import forms 
from .models import Post , Comment # models.py에 있는 class2가지

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post 
        #fields = '__all__'
        exclude = ('user',)

class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment 
        fields = ('content',) # 하나만 입력시에도 , 를 꼭 붙혀야! 