from django.conf.urls import url
from django.urls import path, re_path

from . import views


urlpatterns = [
    #作用修改默认主页
    #path() 参数1：路径(url)    参数2：视图函数函数名(不用加括号)
    path("", views.index),
    path("login", views.login),
    url("^index", views.index),
    url("^register", views.register),
    # url("^login", views.login),
    url("^logout", views.logout),
    url("^infor", views.infor),
    url("^user_basic_infor", views.user_basic_infor),
    url("^consulting_history", views.consulting_history),
    url("^modifyInfor", views.modifyInfor),
    url("^common_medicine", views.common_medicine),
    url("^common_disease", views.common_disease),
    # url("^flush_medicine", views.flush_medicine),
    url("^common_disease", views.common_disease),
    url("^search_symptom", views.search_symptom),
    url("^search_medicine", views.search_medicine),
    url("^test", views.test),
    url("^electric_record", views.electric_record),
    url("^medicine_detail", views.medicine_detail),
    url("^healthy_articles", views.healthy_articles),
    url("^article_detail", views.article_detail),
    url("^headup", views.head_up)






]