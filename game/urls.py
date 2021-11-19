from django.urls import path
from .views import gamePageView

urlpatterns = [
    path("game/", gamePageView, name="game"),
]
