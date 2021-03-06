"""Tests for the models of the ``places`` app."""
from django.test import TestCase

from places.tests.factories import PlaceFactory, PlaceTypeFactory


class PlaceTestCase(TestCase):
    """Tests for the ``Place`` model class."""
    def test_model(self):
        """Should be able to instantiate and save a Place object."""
        instance = PlaceFactory()
        self.assertTrue(instance.pk)

    def test_get_absolute_url(self):
        place = PlaceFactory()
        result = place.get_absolute_url()
        self.assertEqual(result, '/places/1/')


class PlaceTypeTestCase(TestCase):
    """Tests for the ``PlaceType`` model class."""
    def test_model(self):
        """Should be able to instantiate and save a PlaceType object."""
        instance = PlaceTypeFactory()
        self.assertTrue(instance.pk)
