from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from vin_charts.models import (
    Chassis,
    Engine,
    ModelYear,
    Transmission,
    Vehicle
)


class ChassisDetail(DetailView):

    model = Chassis


class EngineDetail(DetailView):

    model = Engine


class ModelYearList(ListView):

    model = ModelYear


class TransmissionDetail(DetailView):

    model = Transmission


class VehicleDetail(DetailView):

    model = Vehicle

    def get_object(self):
        return get_object_or_404(Vehicle, pk=self.kwargs["pk"])


class VehicleList(ListView):

    model = Vehicle
    ordering = ["sales_designation"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["year"] = self.kwargs["model_year"]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.model_year = get_object_or_404(
            ModelYear, year=self.kwargs["model_year"]
        )
        return queryset.filter(model_year=self.model_year)
