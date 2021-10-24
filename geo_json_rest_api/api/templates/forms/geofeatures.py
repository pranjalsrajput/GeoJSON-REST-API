from django import forms

from api.models import GeoFeature


class GeoFeaturesForm(forms.ModelForm):
    class Meta:
        model = GeoFeature
        fields = ('name',)
