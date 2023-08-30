from django.db import models

# Create your models here.
class Post(models.Model): 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ImageField는 Pillow함수가 있어야 사용가능하다. 
    # pip install pillow 
    image = models.ImageField(upload_to='image/')