from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.

class User(AbstractUser): 
    profile_image = ResizedImageField(
        size=[500,500], 
        crop=['middle','center'],
        upload_to='profile',
    ) 
    # posts>modesl.py 파일에 user 추가된 이후로 
    # post_set 생성된거다. 

