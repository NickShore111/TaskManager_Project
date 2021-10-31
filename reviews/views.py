from django.db.models.fields import IntegerField
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from reviews.models import Reviews
from django.views.generic import ListView
from employees.models import Employees, Positions
from django.db.models import Avg
# Create your views here.


# class ReviewListView(ListView):
#     model = Reviews
#     employeeList = Employees.objects.all()
#     positionList = Positions.objects.all()
#     extra_context={
#         'employeeList': employeeList,
#         'positionList': positionList,
#     }

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
    
def review_select(request):
    results = Reviews.objects.all()

    if request.method == "POST":
        if request.POST['position']:
            results = Reviews.objects.filter(employee__position_id=request.POST['position'])

        if request.POST['employee']:
            results = Reviews.objects.filter(employee_id = request.POST['employee'])

    context = {
        "object_list": results,
        'employeeList': Employees.objects.all(),
        'positionList': Positions.objects.all(),
    }
    return render(request, "reviews/reviews_list.html", context)

def review_detail(request,pk):

    avg = dict()
    output = dict()
    total = 0
    count = 0
    employeeReviews = Reviews.objects.filter(employee_id= pk)
    employee = Employees.objects.get(pk=pk)
    fields = Reviews._meta.get_fields(include_parents=False)
    for field in fields:
        if type(field) == IntegerField:
            fieldArr = str(field).split(".")
            avg[fieldArr[2]] = Reviews.objects.all().aggregate(Avg(fieldArr[2]))

    for key, value in avg.items():
        for k,v in value.items():
            output[key] = round(v, 2)

    for key, value in output.items():
        total += value
        count += 1
    output['total'] = round(total/count, 2)

    context = { 
        "object_list": employeeReviews,
        "employee": employee,
        "avg": output,
        "fields": avg,
    }
    return render(request, "reviews/reviews_detail.html", context)
