"""This file is used to read and upload the data from a data file in the .geojson format. The data file is kept
inside the "api/data/" folder. Layer Mapping is used to map the fields in the data file to the columns in the model
where we want to upload the data. """
from django_initialization import start_django

start_django()
import os
from django.contrib.gis.utils import LayerMapping
from api.models import GeoFeature

# map the data fields in the file
municipalities_nl_mapping = {
    'name': 'name',
    'geom': 'MULTIPOLYGON',
}

# Read the data file (.geojson format)
municipalities_nl = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/municipalities_nl.geojson'))


def upload_data(verbose=True):
    """
    Used to read the data file and upload it in the GeoFeature model in the database.
    """
    layer_mapping = LayerMapping(GeoFeature, municipalities_nl, municipalities_nl_mapping, transform=False,
                                 encoding='iso-8859-1')
    layer_mapping.save(strict=True, verbose=verbose)


if __name__ == '__main__':
    upload_data()
