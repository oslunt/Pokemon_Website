from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gamePageView(request) :
    return HttpResponse("This is the games page")