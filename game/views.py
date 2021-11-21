from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gamePageView(request) :
    return render(request, 'game.html')