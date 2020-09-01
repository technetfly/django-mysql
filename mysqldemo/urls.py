"""定义mysqldemo的URL模式"""
from django.conf.urls import url
from django.urls import path
from mysqldemo import views
from django.urls import re_path

urlpatterns = [
    # 主页
    # url django1.x的写法
    # url(r'^show_info/$', views.show_info, name='show_info'),
    # url(r'^add_stu/$', views.add_stu, name='add_stu'),
    # url(r'^del_stu/(?P<id>\d+)/$', views.del_stu, name='del_stu'),
    # url(r'^mod_stu/(?P<id>\d+)/$', views.mod_stu, name='mod_stu'),
    # url(r'^sel_stu/$', views.sel_stu, name='sel_stu'),
    # path是django2.x的写法，re_path与上面正则写法一样
    path('show_info/', views.show_info, name='show_info'),
    path('add_stu/', views.add_stu, name='add_stu'),
    re_path('^del_stu/(\\d+)/$', views.del_stu, name='del_stu'),
    re_path('^mod_stu/(\\d+)/$', views.mod_stu, name='mod_stu'),
    path('sel_stu/', views.sel_stu, name='sel_stu'),
]

app_name = 'mysqldemo'
