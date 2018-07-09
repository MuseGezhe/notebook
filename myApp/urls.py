from django.conf.urls import url
from myApp import views


urlpatterns = [

    url(r'^index/$',views.index),
    #HTML转义
    url(r'^login/$',views.login),

    #验证码
    url(r'verifycode/$',views.verifycode),

]