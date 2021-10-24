from django.contrib import admin

from api.models.features import *


class GeoFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'features')


admin.site.register(GeoFeature, GeoFeatureAdmin)
