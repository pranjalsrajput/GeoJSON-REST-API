"""
This file contains all the common utility functions that are used for the creation of maps.
"""
import folium


def create_map(data_path):
    """Used to create the map from the data. Folium is used to create the map.

    Args:
        data_path: Path to the data file

    Returns:
        The html object of the created map.
    """
    geo_data_map = folium.Map(location=[53.2194, 6.5665], zoom_start=6)
    style = {'fillColor': '#228B22', 'color': '#228B22'}
    folium.GeoJson(data_path, name='municipalities_nl', style_function=lambda x: style).add_to(geo_data_map)
    folium.LayerControl().add_to(geo_data_map)
    geo_data_map = geo_data_map._repr_html_()
    return geo_data_map
