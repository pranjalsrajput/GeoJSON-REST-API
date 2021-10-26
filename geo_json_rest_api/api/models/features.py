from django.db import models as dbModels
from django.contrib.gis.db import models


class GeoFeature(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326, null=True, blank=True, )
    objects = dbModels.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
