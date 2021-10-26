from django.contrib import admin

from api.models.features import *
from leaflet.admin import LeafletGeoAdmin


class GeoFeatureAdmin(LeafletGeoAdmin):
    list_display = ('id', 'name', 'geom')


admin.site.register(GeoFeature, GeoFeatureAdmin)
