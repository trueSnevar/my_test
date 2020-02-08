from django.db import models

# Create your models here.


class TruckModel(models.Model):
    model_name = models.CharField(max_length=200)
    weight_capacity = models.FloatField()

    def __str__(self):
        return self.model_name


class Truck(models.Model):
    garage_number = models.CharField(max_length=200)
    model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)
    current_weight = models.FloatField(default=0)

    @property
    def check_overload(self):
        if self.current_weight > self.model.weight_capacity:
            overweight = round((self.current_weight / self.model.weight_capacity) * 100, 2)
            return round((overweight - 100), )

        return 0

    def __str__(self):
        return self.garage_number
