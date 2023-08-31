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
    # post_set = 생성
    # like_posts = 생성 
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # 여기서 self 는 자기자신 user이긴한데, user라고 적으면 자기자신재귀가 빠져서 self라고 
    # 여기서 makemigration,migrate 작업하게되면 user_set이 db 컬럼으로 생성되는데, 
    # 우리는 헷갈리니까 자동생성되는 이 이름 수정할거야. followers 로! 
    # symmetrical 은 대칭이란 뜻으로, 
    # 유저 <---둘다팔로우---> 유저  로 쌍방향이 아닌, 
    # 유저 <--한사람만팔로우-- 유저  로 한방향으로 ! 
    