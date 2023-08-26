from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(requests):
    return HttpResponse("这里是我的投票站点！")
