from django.conf.urls import url
from django.urls import  path
from . import views

urlpatterns = [
    #作用修改默认主页
    path("", views.index),
    url("^index",views.index),
    url("^register", views.register),
    url("^login", views.login),
    url("^logout",views.logout)

]