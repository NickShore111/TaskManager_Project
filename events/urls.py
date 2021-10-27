from django.urls import path
from events import views
from events.views import *

app_name = "events"
urlpatterns = [
    path("", views.calendar_view, name='index'),
    path("<day__gte>", views.calendar_view),
    path("detail/", EventListView.as_view(), name='detail'),
    path("create/", EventCreateView.as_view(), name='create'),
    path("update/", EventUpdateView.as_view(), name='update'),
    path("delete/", EventDeleteView.as_view(), name='delete'),
]
