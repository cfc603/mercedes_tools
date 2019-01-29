from django.urls import reverse
from django.test import TestCase

from model_mommy import mommy


class ChassisModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("vin_charts.Chassis")

        # tests
        self.assertEqual(obj.__str__(), obj.number)


class EngineModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("vin_charts.Engine")

        # tests
        self.assertEqual(obj.__str__(), obj.number)


class ModelYearModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("vin_charts.ModelYear")

        # tests
        self.assertEqual(obj.__str__(), str(obj.year))


class TransmissionModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("vin_charts.Transmission")

        # tests
        self.assertEqual(obj.__str__(), obj.number)


class VehicleModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("vin_charts.Vehicle")

        # tests
        self.assertEqual(
            obj.__str__(), f"{obj.model_year.year} {obj.sales_designation}"
        )

    def test_get_absolute_url(self):
        # setup
        obj = mommy.make("vin_charts.Vehicle")

        # tests
        self.assertEqual(
            obj.get_absolute_url(),
            reverse(
                "vin_charts:vehicle_detail", args=[obj.slug(), str(obj.id)]
            )
        )

    def test_slug(self):
        # setup
        obj = mommy.make(
            "vin_charts.Vehicle",
            model_year=mommy.make("vin_charts.ModelYear", year=2018),
            sales_designation="CLA250"
        )

        # asserts
        self.assertEqual(obj.slug(), "2018-cla250")
