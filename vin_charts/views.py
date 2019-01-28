from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from vin_charts.models import ModelYear, Vehicle


class ModelYearList(ListView):

    model = ModelYear


class VehicleDetail(DetailView):

    model = Vehicle

    def get_object(self):
        return get_object_or_404(Vehicle, pk=self.kwargs["pk"])


class VehicleList(ListView):

    model = Vehicle

    def get_queryset(self):
        queryset = super().get_queryset()
        self.model_year = get_object_or_404(
            ModelYear, year=self.kwargs["model_year"]
        )
        return queryset.filter(model_year=self.model_year)
