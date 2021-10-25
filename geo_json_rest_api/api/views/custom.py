from django.shortcuts import render, get_object_or_404

# def say_hello(request):
#     return render(request, 'hello.html')
from api.models import GeoFeature
from api.serializers.features import GeoFeatureSerializer
from api.templates.forms.geofeatures import GeoFeaturesForm
from api.utils.maps import create_map


# Create your views here.
# def say_hello(request):
#     return HttpResponse("Hello world")


def visualize_geo_data(request):
    data_path = 'api/data/municipalities_nl.geojson'
    geo_data_map = create_map(data_path)
    context = {'geo_data_map': geo_data_map}
    return render(request, 'pages/home.html', context)


def geofeature_list_view(request):
    queryset = GeoFeature.objects.all().order_by("id")
    # queryset = get_object_or_404(GeoFeature,  id=1)
    form = GeoFeaturesForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False) # We don't want to save form at this point
        instance.name = form.cleaned_data.get('name') # Coming through the form
        form.save()
    context = {
        'object_list': queryset,
        'form': form
    }
    return render(request, 'pages/geofeatures.html', context)

