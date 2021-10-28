from django.urls import path
from .views import indexPageView
from .views import leaderboardPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("Leaderboard", leaderboardPageView, name="leaderboard"),
]
