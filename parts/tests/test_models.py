from django.test import TestCase

from model_mommy import mommy


class PartModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("parts.Part")

        # setup
        self.assertEqual(obj.__str(), obj.sku)


class PartModelTest(TestCase):

    def test_str(self):
        # setup
        obj = mommy.make("parts.Type")

        # setup
        self.assertEqual(obj.__str(), obj.description)
