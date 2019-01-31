from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Chassis(models.Model):

    number = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.number


class Engine(models.Model):

    number = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.number


class ModelYear(models.Model):

    year = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return str(self.year)

    class Meta:
        ordering = ["-year",]


class Transmission(models.Model):

    number = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return self.number


class Vehicle(models.Model):

    model_year = models.ForeignKey("ModelYear", on_delete=models.PROTECT)
    vin_prefix = models.CharField(max_length=10, unique=True)
    sales_designation = models.CharField(max_length=120)
    chassis = models.ForeignKey("Chassis", on_delete=models.PROTECT)
    engine = models.ForeignKey("Engine", on_delete=models.PROTECT)
    transmissions = models.ManyToManyField("Transmission")

    def __str__(self):
        return f"{self.model_year.year} {self.sales_designation}"

    def get_absolute_url(self):
        return reverse(
            "vin_charts:vehicle_detail", args=[self.slug(), str(self.id)]
        )

    def slug(self):
        return slugify(f"{self.model_year.year} {self.sales_designation}")
