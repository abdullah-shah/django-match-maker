"""Admin classes for the ``places`` app."""
from django.conf import settings
from django.contrib.gis import admin
from django.db.models.options import Options

import reversion

from places.models import Place, PlaceType


Options.get_ordered_objects = lambda x: None


class GoogleMapsAdmin(reversion.VersionAdmin, admin.OSMGeoAdmin):
    map_template = 'gis/admin/google.html'
    openlayers_url = '{0}places/js/libs/openlayers/OpenLayers.js'.format(
        settings.STATIC_URL)
    extra_js = [
        'https://maps.googleapis.com/'
        'maps/api/js?key={0}&sensor=false'.format(
            settings.GOOGLE_MAPS_API_KEY),
    ]


admin.site.register(Place, GoogleMapsAdmin)
admin.site.register(PlaceType)
