from django.urls import path
from . import views
from reviews.views import *

app_name = "reviews"
urlpatterns = [
    path("", ReviewListView.as_view(), name='list'),
    path("detail/<int:pk>/", ReviewListView.as_view(), name='detail'),
    path("create/", ReviewCreateView.as_view(), name='add'),
    path("update/", ReviewUpdateView.as_view(), name='update'),
    path("delete/", ReviewDeleteView.as_view(), name='delete'),
]
