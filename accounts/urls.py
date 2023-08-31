from django.urls import path
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('<str:username>/', views.profile, name='profile'),
    # 여기에는 accounts/가 앞에 생략되었다. 
    path('<str:username>/follow',views.follow,name='follow'),
]