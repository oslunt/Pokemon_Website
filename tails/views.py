from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexPageView(request) :
    return render(request, 'tails/index.html')

def leaderboardPageView(request) :
    return render(request, "tails/leaderboard.html")