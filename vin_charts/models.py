from django.db import models


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
    transmission = models.ForeignKey("Transmission", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.model_year.year} {self.sales_designation}"
