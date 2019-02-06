from django.db import models

from vin_charts.models import Chassis, Engine, Transmission


class Part(models.Model):

    sku = models.CharField(max_length=50, unique=True)
    type = models.ForeignKey("Type", on_delete=models.PROTECT)
    chassis = models.ManyToManyField(Chassis)
    engines = models.ManyToManyField(Engine)
    transmissions = models.ManyToManyField(Transmission)

    def __str__(self):
        return self.sku


class Type(models.Model):

    description = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.description
