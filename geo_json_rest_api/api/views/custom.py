"""This file contains the custom views used in the application.
"""
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from api.models import GeoFeature
from api.utils.maps import create_map


def visualize_geo_data(request):
    """This is used to visualize the geofeature data. It reads the data from the .geojson file, creates the map from
    the data and renders the result on a webpage.
    """
    data_path = 'api/data/municipalities_nl.geojson'
    geo_data_map = create_map(data_path)
    context = {'geo_data_map': geo_data_map}
    return render(request, 'pages/home.html', context)


def geofeature_list_view(request):
    """This is used to get the list of geofeatures, and renders the result on webpage.
    """
    queryset = GeoFeature.objects.all().order_by("id")
    context = {
        'object_list': queryset,
    }
    return render(request, 'pages/geofeatures.html', context)


class UpdateFeatures(generics.GenericAPIView):
    """This is used to update the features in GeoFeature model from frontend.
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
