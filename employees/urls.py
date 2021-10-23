from django.urls import path
from . import views

app_name = "employees"
urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<employeePK>", views.edit, name="edit"),
    path("edit/update/<employeePK>", views.update, name="update"),
    path("edit/delete/<employeePK>", views.delete, name="delete"),
    path("edit/create/", views.create, name="create"),

]
