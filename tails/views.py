from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexPageView(request) :
    return HttpResponse("This is the index page")

def leaderboardPageView(request) :
    return HttpResponse("This is the leaderboard page")