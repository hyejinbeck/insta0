from django.db import models
from django_resized import ResizedImageField # 이미지크롭화
from django.conf import settings

# Create your models here.
class Post(models.Model): 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # image = models.ImageField(upload_to='image/%Y/%m')
    # 그리고 이걸 추가 
    image = ResizedImageField(
        size=[500,500],
        crop=['middle', 'center'], 
        upload_to='image/%Y/%m', 
    )  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user 추가함으로서, accounts의 Modes.py와 1:N 연결 
    # user_id가 생성된거다. 

class Comment(models.Model): 
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # 1:N 연결
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    