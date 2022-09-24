"""Project_database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
urls_teach=include("teach.urls")
urls_frontend=include("frontend.urls")
urls_user=include("app_users.urls")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("django.contrib.auth.urls")),
    path('teach/', urls_teach),
    path('', urls_frontend),
    path('',urls_user),
]
