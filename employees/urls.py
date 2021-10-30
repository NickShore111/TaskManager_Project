from django.urls import path
from . import views
from employees.views import *

app_name = "employees"
urlpatterns = [
    path("", views.index, name="index"),
    path("form/", EmployeeFormView.as_view(), name="form"),
    path("create/", EmployeeCreateView.as_view(), name="create"),
    path("list/", EmployeeListView.as_view(), name="list"),
    path("update/<int:pk>", EmployeeUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", EmployeeDeleteView.as_view(), name="delete"),
    # path("edit/<employeePK>", views.edit, name="edit"),

]
