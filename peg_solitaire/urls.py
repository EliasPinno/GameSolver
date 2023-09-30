from django.urls import path

from .views import solution_view

urlpatterns = [
    path("", solution_view, name="pegSolitaireUrl"),
]
