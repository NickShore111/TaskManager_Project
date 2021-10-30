from django.urls import path
from reviews.views import *
from . import views

app_name = "reviews"
urlpatterns = [
    path("", views.review_select, name='index'),
    path("<int:pk>/", views.review_detail, name='detail'),
    path("create/", ReviewCreateView.as_view(), name='create'),
    path("update/", ReviewUpdateView.as_view(), name='update'),
    path("delete/", ReviewDeleteView.as_view(), name='delete'),
    path("select/", views.review_select, name='select'),
]
