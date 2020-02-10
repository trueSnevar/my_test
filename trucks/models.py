from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here.


def validate_zero(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s является недопустимым значением'),
            params={'value': value},
        )


class TruckModel(models.Model):
    model_name = models.CharField(max_length=200)
    weight_capacity = models.FloatField(blank=False, default=100, validators=[validate_zero])

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
