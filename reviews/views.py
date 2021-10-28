from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from reviews.models import Reviews
from django.views.generic import ListView
from employees.models import Employees
# Create your views here.


class ReviewListView(ListView):
    model = Reviews
    employeeList = Employees.objects.all()
    extra_context={'employeeList': employeeList}

    # add context = {"EmployeeList": Employees.objects.all() }


class ReviewCreateView(CreateView):
    model = Reviews
    fields = '__all__'

class ReviewUpdateView(UpdateView):
    model = Reviews
    fields = '__all__'

class ReviewDeleteView(DeleteView):
    model = Reviews
    fields = '__all__'
    success_url = reverse_lazy('review-form')


def review_detail(request,pk):

    employeeReviews = Reviews.objects.filter(employee_id= pk)
    employee = Employees.objects.get(pk=pk)
    context = { "object_list": employeeReviews,
                "employee": employee}
    return render(request, "reviews/reviews_detail.html", context)