from django.urls import path
from . import views

app_name = "employees"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("update/", views.update, name="update"),
    path("update/<employeePK>", views.update, name="update"),
    path("delete/<employeePK>", views.delete, name="delete"),
    # path("edit/<employeePK>", views.edit, name="edit"),

]
