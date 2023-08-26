# -*- coding:utf-8 -*-
# author: vetra


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
