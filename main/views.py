from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render('<p>main/index.html</p>')


def about(request):
    return HttpResponse('<h4>about</h4>')