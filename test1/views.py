#coding=utf-8
from django.http import HttpResponse


def user_view(request):
    return HttpResponse('123')