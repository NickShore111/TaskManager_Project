from django.urls import path
from . import views

app_name = "taskEvents"
urlpatterns = [
    path("", views.index),
]
