from django.urls import path,include
from .views import *


urlpatterns = [
    # path('',include("django.contrib.auth.urls")),
    #ฟอร์ม หลังlogin
    path('user/course/', home, name="home"),
    path('register/', register,name='register'),
    path('dashboard/', dashboard ,name='dashboard'),

]