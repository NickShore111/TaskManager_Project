from django.db.models import fields
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render
from reviews.models import Review
from django.views.generic import ListView

# Create your views here.


class ReviewListView(ListView):
    model = Review
class ReviewCreateView(CreateView):
    model = Review
    fields = '__all__'

class ReviewUpdateView(UpdateView):
    model = Review
    fields = '__all__'

class ReviewDeleteView(DeleteView):
    model = Review
    fields = '__all__'
    success_url = reverse_lazy('review-form')

