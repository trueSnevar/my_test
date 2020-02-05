from django.db import models

# Create your models here.


class TruckModel(models.Model):
    model_name = models.CharField(max_length=200)
    weight_capacity = models.FloatField()


class Truck(models.Model):
    garage_number = models.FloatField(unique=True)
    model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)

