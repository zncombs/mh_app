from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home/$', views.index, name="home"),
    url(r'^blog/$', views.blog, name="blog"),
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^learnmore/$', views.learnmore, name="learnmore"),
    url(r'^contact/$', views.contact, name="contact"),

]
