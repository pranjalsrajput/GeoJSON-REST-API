from rest_framework import serializers

from api.models import *


class GeoFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoFeature
        fields = "__all__"
