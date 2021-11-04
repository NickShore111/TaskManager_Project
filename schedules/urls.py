from django.urls import path
from schedules import views
from schedules.views import *

app_name = "schedules"
urlpatterns = [
    path("list/", ShiftListView.as_view(), name='list'),
    path("create/", views.schedule_form, name='create'),
    # path("select/<int:date>", views.schedule_select, name='select-schedule'),
    path("update/<int:pk>", ShiftUpdateView.as_view(), name='update'),
    path("delete/<int:pk>", views.shift_delete, name='delete'),
    path("create-schedule", views.create_schedule, name='create-schedule'),

    
]
