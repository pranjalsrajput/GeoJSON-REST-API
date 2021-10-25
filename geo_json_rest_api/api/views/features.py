from django.contrib.gis.geos import Point
from rest_framework import permissions, viewsets, generics
from rest_framework.response import Response

from api.models import *
from api.serializers.features import GeoFeatureSerializer


class GeoFeatureAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = GeoFeature.objects.all()
    serializer_class = GeoFeatureSerializer


class BoundingBoxFilter(generics.GenericAPIView):

    def get(self, request):
        coordinates = request.GET.get('bbox')
        coordinates = coordinates.split(",")
        point = Point(float(coordinates[0]), float(coordinates[1]))
        geo_feature_list = GeoFeature.objects.filter(geom__contains=point)
        serialized_data = GeoFeatureSerializer(geo_feature_list, many=True).data
        return Response({"filtered_data": serialized_data})
