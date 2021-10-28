from django.urls import path
from .views import crudPageView

urlpatterns = [
    path("", crudPageView, name="crud")
]
