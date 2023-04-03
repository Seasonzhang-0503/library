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
    path('', views.home, name='home'),

    # location增删改查
    path('locationlist_show/', views.locationlist_show, name='locationlist_show'),
    path('locationlist_new/', views.locationlist_new, name='locationlist_new'),
    path('locationlist_edit/<int:lid>/', views.locationlist_edit,name='locationlist_edit'),
    path('locationlist_delete/<int:lid>/', views.locationlist_delete,name='locationlist_delete'),
    
    # category增删改查
    path('categorylist_show/', views.categorylist_show, name='categorylist_show'),
    path('categorylist_new/', views.categorylist_new, name='categorylist_new'),
    path('categorylist_edit/<int:cid>/', views.categorylist_edit,name='categorylist_edit'),
    path('categorylist_delete/<int:cid>/', views.categorylist_delete,name='categorylist_delete'),

    # theBook增删改查
    # path('theBooklist_show/', views.theBooklist_show, name='theBooklist_show'),
    path('theBooklist_show/<int:page>/',views.theBooklist_show,name='theBooklist_show'),
    path('getQueryBookForm/', views.getQueryBookForm, name='getQueryBookForm'),
    path('theBooklist_new/', views.theBooklist_new, name='theBooklist_new'),
    path('theBooklist_edit/<int:bid>/', views.theBooklist_edit,name='theBooklist_edit'),
    path('theBooklist_delete/<int:bid>/', views.theBooklist_delete,name='theBooklist_delete'),

    # theBorrow增删改查
    path('theBorrowlist_show/', views.theBorrowlist_show, name='theBorrowlist_show'),
    path('theBorrowlist_show/<int:page>/', views.theBorrowlist_show, name='theBorrowlist_show'),
    path('theBorrowlist_new/', views.theBorrowlist_new, name='theBorrowlist_new'),
    path('theBorrowlist_edit/<int:boid>/', views.theBorrowlist_edit,name='theBorrowlist_edit'),
    path('theBorrowlist_delete/<int:boid>/', views.theBorrowlist_delete,name='theBorrowlist_delete'),
    path('theBorrowlist_new_default/<int:bid>/', views.theBorrowlist_new_default,name='theBorrowlist_new_default'),

    
    # theUser增删改查
    path('theUserlist_show/', views.theUserlist_show, name='theUserlist_show'),
    path('theUserlist_show/<int:page>/', views.theUserlist_show, name='theUserlist_show'),
    path('theUserlist_new/', views.theUserlist_new, name='theUserlist_new'),
    path('theUserlist_edit/<int:id>/', views.theUserlist_edit,name='theUserlist_edit'),
    path('theUserlist_delete/<int:id>/', views.theUserlist_delete,name='theUserlist_delete'),

    # theBorrow_user增删改查
    path('theBorrowlist_user/', views.theBorrowlist_user, name='theBorrowlist_user'),
    path('theBorrowlist_user_modal_show/', views.theBorrowlist_user_modal_show, name='theBorrowlist_user_modal_show'),
    path('theBorrowlist_user_modal_new/', views.theBorrowlist_user_modal_new, name='theBorrowlist_user_modal_new'),


    # 登录相关
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),


    
    ##　静态文件夹路由：读取"/static/"的数据
    re_path('static/(?P<path>.*)', serve, {'document_root':settings.STATIC_ROOT},name='static'),
    ##　媒体文件夹路由：读取"/static/"的数据
    re_path('media/(?P<path>.*)', serve, {'document_root':settings.MEDIA_ROOT},name='media'),
]
