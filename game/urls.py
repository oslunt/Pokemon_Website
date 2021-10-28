from django.urls import path
from .views import gamePageView

urlpatterns = [
    path("", gamePageView, name="game"),
]
