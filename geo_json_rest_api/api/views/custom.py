from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from api.models import GeoFeature
from api.utils.maps import create_map


def visualize_geo_data(request):
    data_path = 'api/data/municipalities_nl.geojson'
    geo_data_map = create_map(data_path)
    context = {'geo_data_map': geo_data_map}
    return render(request, 'pages/home.html', context)


def geofeature_list_view(request):
    queryset = GeoFeature.objects.all().order_by("id")
    context = {
        'object_list': queryset,
    }
    return render(request, 'pages/geofeatures.html', context)


class UpdateFeatures(generics.GenericAPIView):
    """
    """

    def post(self, request):
        try:
            GeoFeature.objects.filter(pk=request.data['row_id']).update(name=request.data['row_val'])
            return Response({
                "state": "success"
            }
            )
        except Exception as e:
            print("Error:{}".format(e))
