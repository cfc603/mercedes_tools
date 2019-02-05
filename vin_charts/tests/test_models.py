from django.urls import reverse
from django.test import TestCase

from mock import Mock
from model_mommy import mommy

from vin_charts.models import Note


class ChassisModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("vin_charts.Chassis")

        # tests
        self.assertEqual(obj.__str__(), obj.number)

    def test_get_absolute_url(self):
        # setup
        obj = mommy.make("vin_charts.Chassis")

        # tests
        self.assertEqual(
            obj.get_absolute_url(),
            reverse(
                "vin_charts:chassis_detail", args=[obj.slug(), str(obj.id)]
            )
        )

    def test_slug(self):
        # setup
        obj = mommy.make("vin_charts.Chassis", number="123.123")

        # asserts
        self.assertEqual(obj.slug(), "123123")


class EngineModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("vin_charts.Engine")

        # tests
        self.assertEqual(obj.__str__(), obj.number)

    def test_get_absolute_url(self):
        # setup
        obj = mommy.make("vin_charts.Engine")

        # tests
        self.assertEqual(
            obj.get_absolute_url(),
            reverse(
                "vin_charts:engine_detail", args=[obj.slug(), str(obj.id)]
            )
        )

    def test_slug(self):
        # setup
        obj = mommy.make("vin_charts.Engine", number="123.123")

        # asserts
        self.assertEqual(obj.slug(), "123123")


class ModelYearModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("vin_charts.ModelYear")

        # tests
        self.assertEqual(obj.__str__(), str(obj.year))


class NoteModelTest(TestCase):

    def test_create_from_import_if_not_message(self):
        # setup
        obj = Mock()
        Note.create_from_import(obj, None)

        # asserts
        obj.notes.all.assert_not_called()
        obj.notes.add.assert_not_called()

    def test_create_from_import_if_previously_created(self):
        # setup
        notes = Mock()
        notes.all.return_value = [Mock(message="message")]
        obj = Mock(notes=notes)
        Note.create_from_import(obj, "message")

        # asserts
        obj.notes.all.assert_called_once()
        self.assertFalse(Note.objects.exists())
        obj.notes.add.assert_not_called()

    def test_create_from_import_if_not_previously_created(self):
        # setup
        notes = Mock()
        notes.all.return_value = [Mock(message="message")]
        obj = Mock(notes=notes)
        note = Note.create_from_import(obj, "new message")

        # asserts
        obj.notes.all.assert_called_once()
        self.assertEqual(Note.objects.all().count(), 1)
        self.assertEqual(note.message, "new message")
        obj.notes.add.assert_called_once_with(note)


class TransmissionModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("vin_charts.Transmission")

        # tests
        self.assertEqual(obj.__str__(), obj.number)

    def test_get_absolute_url(self):
        # setup
        obj = mommy.make("vin_charts.Transmission")

        # tests
        self.assertEqual(
            obj.get_absolute_url(),
            reverse(
                "vin_charts:transmission_detail",
                args=[obj.slug(), str(obj.id)]
            )
        )

    def test_slug(self):
        # setup
        obj = mommy.make("vin_charts.Transmission", number="123.123")

        # asserts
        self.assertEqual(obj.slug(), "123123")


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
