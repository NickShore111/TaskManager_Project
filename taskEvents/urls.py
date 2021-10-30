from django.urls import path
from . import views
from taskEvents.views import *

app_name = "taskEvents"
urlpatterns = [
    # path("", views.index),
    path("create/", TaskCreateView.as_view(), name = 'create'),
]
