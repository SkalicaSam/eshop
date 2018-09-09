from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hey Client, my app is running")