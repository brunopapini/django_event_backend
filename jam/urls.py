"""jam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from jam1.views import  EventApiView 
from django.urls import path
from django.contrib import admin
from jam1 import views
#from rest_framework.authtoken import views as view




urlpatterns = [
    

   	path('event', views.EventApiView.as_view()),

   	path('event1', views.EventApiViewAuth.as_view()),
   	
    path('api/<int:pk>/', views.DetailEventApiView.as_view()),

    
    path('rest-auth/', include('rest_auth.urls')),

    path('admin/', admin.site.urls),

    path('user1/', views.UserApiView.as_view()),

]






   	#url(r'^api-token-auth/', view.obtain_auth_token),

   	#path('admin/', admin.site.urls),
    
   	#path('user1/', views.UserApiView.as_view()),

   	#path('users', views.ListUsers.as_view()),


#UserViewSet