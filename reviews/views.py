from django.db.models import fields
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from reviews.models import Reviews
from django.views.generic import ListView

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

