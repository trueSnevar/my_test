from django.shortcuts import render
from django.http import HttpResponse
from .models import TruckModel, Truck
from django.template import loader
# Create your views here.


def is_valid_queryparam(param):
    return param != '' and param is not None


def index(request):
    truck_list = Truck.objects.all()
    models = TruckModel.objects.all()
    model = request.GET.get('model')

    if is_valid_queryparam(model) and model != "Все":
        truck_list = truck_list.filter(model=model)

    context = {
        'truck_list': truck_list,
        'models': models
    }
    return render(request, 'trucks/index.html', context)
