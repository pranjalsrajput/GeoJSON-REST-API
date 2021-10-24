# from django.db import models
from django.db import models as dbModels
from django.contrib.gis.db import models


class GeoFeature(models.Model):
    features = models.JSONField(null=True, blank=True, default=dict)
    point = models.PointField(null=True, blank=True)
    objects = dbModels.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
