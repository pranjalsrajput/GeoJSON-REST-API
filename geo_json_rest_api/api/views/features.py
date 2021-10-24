from rest_framework import permissions, viewsets

from api.models import *
from api.serializers.features import GeoFeatureSerializer


class GeoFeatureAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = GeoFeature.objects.all()
    serializer_class = GeoFeatureSerializer

