from django.test import TestCase

from mock import patch

from vin_charts.models import ModelYear, Vehicle
from vin_charts.views import VehicleDetail, VehicleList


class VehicleListViewTest(TestCase):

    @patch("vin_charts.views.get_object_or_404")
    def test_get_object(self, get_object_or_404):
        # setup
        view = VehicleDetail()
        view.kwargs = {"pk": 1}
        obj = view.get_object()

        # asserts
        get_object_or_404.assert_called_once_with(Vehicle, pk=1)
        self.assertEqual(obj, get_object_or_404(Vehicle, pk=1))

    @patch("vin_charts.views.ListView.get_queryset")
    @patch("vin_charts.views.get_object_or_404", return_value=1234)
    def test_get_queryset(self, get_object_or_404, get_queryset):
        # setup
        view = VehicleList()
        view.kwargs = {"model_year": 5678}
        queryset = view.get_queryset()

        # asserts
        get_object_or_404.assert_called_once_with(ModelYear, year=5678)
        get_queryset().filter.assert_called_once_with(model_year=1234)
        self.assertEqual(queryset, get_queryset().filter(model_year=1234))
