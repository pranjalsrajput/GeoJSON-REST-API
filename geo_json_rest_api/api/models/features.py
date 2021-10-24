# from django.db import models
from django.db import models as dbModels
from django.contrib.gis.db import models


# class GeoFeature(models.Model):
#     features = models.JSONField(null=True, blank=True, default=dict)
#     point = models.PointField(null=True, blank=True)
#     objects = dbModels.Manager()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class GeoFeature(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326, null=True, blank=True,)
    objects = dbModels.Manager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #
    # def __str__(self):
    #     return self.name
