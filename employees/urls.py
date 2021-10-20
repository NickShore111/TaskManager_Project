from django.urls import path
from . import views

app_name = "employees"
urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<employeePK>", views.edit, name="edit"),
    path("update/<employeePK>", views.update, name="update"),
    # path("display/<employeePK>", views.view_or_edit, name="view-edit"),
]
