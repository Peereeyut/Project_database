from django.urls import path,include
from .views import *


urlpatterns = [
    path('user/course/', home,),
    path('register/', register,name='register'),
    path('dashboard/', dashboard ,name='dashboard'),
    path('profile/', profile, name='profile'),
    path('course/', course, )
]