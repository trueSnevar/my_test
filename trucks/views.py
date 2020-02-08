from django.shortcuts import render
from django.http import HttpResponse
from .models import TruckModel, Truck
from django.template import loader
# Create your views here.


def index(request):
    truck_list = Truck.objects.all()
    context = {'truck_list': truck_list}
    return render(request, 'trucks/index.html', context)
