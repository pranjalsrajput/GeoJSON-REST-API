from django_initialization import start_django

start_django()
import os
from django.contrib.gis.utils import LayerMapping
from api.models import GeoFeature

municipalities_nl_mapping = {
    'name': 'name',
    'geom': 'MULTIPOLYGON',
}

municipalities_nl = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/municipalities_nl.geojson'))


def upload_data(verbose=True):
    layer_mapping = LayerMapping(GeoFeature, municipalities_nl, municipalities_nl_mapping, transform=False,
                                 encoding='iso-8859-1')
    layer_mapping.save(strict=True, verbose=verbose)


if __name__ == '__main__':
    upload_data()
