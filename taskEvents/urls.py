from django.urls import path
from . import views
from taskEvents.views import *

app_name = "taskEvents"
urlpatterns = [
    path("list/", TaskListView.as_view(), name = 'list'),
    path("create/", TaskCreateView.as_view(), name = 'create'),
    path("update/<int:pk>", TaskUpdateView.as_view(), name = 'update'),
    path("delete/<int:pk>", views.delete_task, name = 'delete'),
    path("select/", views.task_select, name = 'select'),
]
