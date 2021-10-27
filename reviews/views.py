from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import generic
from reviews.models import Reviews
from django.views.generic import ListView
from employees.models import Employees

# Create your views here.


class ReviewListView(ListView):
    model = Reviews
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


# class ReviewDetailView(generic.DetailView):
#     model = Reviews
#     template_name = "reviews/reviews_list.html"
#     context_object_name = "object_list"


def review_list(request,pk):
    employeeReviews = Reviews.objects.filter(employee_id= pk)
    print(Employees.objects.get(pk=pk))
    print(employeeReviews)
    context = { "object_list": employeeReviews}
    return render(request, "reviews/reviews_detail.html", context)