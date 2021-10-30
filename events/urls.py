from django.urls import path
from events import views
from events.views import *

app_name = "events"
urlpatterns = [
    path("", views.calendar_view, name='index'),
    path("<day__gte>", views.calendar_view),
    path("list/", EventListView.as_view(), name='list'),
    path("form/", EventFormView.as_view(), name='form'),
    path("create/", EventCreateView.as_view(), name='create'),
    path("update/", EventUpdateView.as_view(), name='update'),
    path("update/<int:pk>", EventUpdateView.as_view(), name='update'),
    path("delete/<int:pk>", views.delete_event, name='delete'),
]
