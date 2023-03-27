"""library URL Configuration

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
from django.urls import path
from book import views
from . import settings
from django.conf.urls import url 
from django.urls import re_path
from django.views.static import serve
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.categorylist, name='categorylist'),
    path('categorylist_show/', views.categorylist_show, name='categorylist_show'),
    path('categorylist_new/', views.categorylist_new, name='categorylist_new'),
    path('categorylist_edit/<int:cid>/', views.categorylist_edit,name='categorylist_edit'),
    path('categorylist_delete/<int:cid>/', views.categorylist_delete,name='categorylist_delete'),

    
    ##　静态文件夹路由：读取"/static/"的数据
    re_path('static/(?P<path>.*)', serve, {'document_root':settings.STATIC_ROOT},name='static'),
    ##　媒体文件夹路由：读取"/static/"的数据
    re_path('media/(?P<path>.*)', serve, {'document_root':settings.MEDIA_ROOT},name='media'),
]
