"""This file contains the api views for geofeature model.
"""

from django.contrib.gis.geos import Point
from rest_framework import viewsets, generics
from rest_framework.response import Response

from api.models import *
from api.serializers.features import GeoFeatureSerializer


class GeoFeatureAPI(viewsets.ModelViewSet):
    queryset = GeoFeature.objects.all()
    serializer_class = GeoFeatureSerializer


class BoundingBoxFilter(generics.GenericAPIView):
    """This is used for filtering the geofeature model data by bounding box coordinate.

    Returns:
        The filtered serialized data in response.
    """

    def get(self, request):
        coordinates = request.GET.get('bbox')  # Get the coordinate value from request
        coordinates = coordinates.split(",")  # Get the coordinates
        point = Point(float(coordinates[0]), float(coordinates[1]))  # Typecast to Point
        geo_feature_list = GeoFeature.objects.filter(geom__contains=point)  # Filter the records that contain the point
        serialized_data = GeoFeatureSerializer(geo_feature_list, many=True).data
        return Response({"filtered_data": serialized_data})
