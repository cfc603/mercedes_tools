from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from vin_charts.models import ModelYear, Vehicle


class ModelYearList(ListView):

    model = ModelYear


class VehicleList(ListView):

    model = Vehicle

    def get_queryset(self):
        queryset = super().get_queryset()
        self.model_year = get_object_or_404(ModelYear, year=self.kwargs["model_year"])
        return queryset.filter(model_year=self.model_year)
