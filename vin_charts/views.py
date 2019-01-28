from django.views.generic import ListView

from vin_charts.views import ModelYear


class ModelYearList(ListView):

    model = ModelYear
