from django.urls import path
from schedules import views
from schedules.views import *

app_name = "schedules"
urlpatterns = [
    path("list/", ScheduleListView.as_view(), name='list'),
    path("create/", ScheduleCreateView.as_view(), name='create'),
    path("update/<int:pk>", ScheduleUpdateView.as_view(), name='update'),
    path("delete/<int:pk>", views.shift_delete, name='delete'),

]
