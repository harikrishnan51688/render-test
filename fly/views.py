from django.shortcuts import render

# Create your views here.

# fly/views.py
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, Fly!")
