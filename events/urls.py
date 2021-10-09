from django.urls import path
from events import views

app_name = 'events'
urlpatterns = [
    path('', views.calendar_view),
    path('<day__gte>', views.calendar_view),

]