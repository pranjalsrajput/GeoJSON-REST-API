import folium


def create_map(data_path):
    geo_data_map = folium.Map(location=[-16.22, -71.59], zoom_start=2)
    style = {'fillColor': '#228B22', 'color': '#228B22'}
    folium.GeoJson(data_path, name='municipalities_nl', style_function=lambda x: style).add_to(geo_data_map)
    folium.LayerControl().add_to(geo_data_map)
    geo_data_map = geo_data_map._repr_html_()
    return geo_data_map
