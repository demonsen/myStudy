
from django.urls import path, re_path
from . import views, testdb

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index),
    path('logout/', views.logout, name='logout'),
    path('order/', views.order),
    path('test/', views.test, name='test'),
    path('testdb/', testdb.testdb),
    re_path('^xx/([0-9]{4})/$', views.xx), 
]
