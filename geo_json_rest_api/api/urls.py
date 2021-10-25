"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from api.views import GeoFeatureAPI
from api.views.custom import *
from api.views.features import BoundingBoxFilter

router = routers.DefaultRouter()

# Basic rest API for all models
router.register("api/feature", GeoFeatureAPI, "geofeature"),
# router.register("api/boundingboxfilter", BoundingBoxFilter, "boundingboxfilter"),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
    path('api/token/verify', TokenVerifyView.as_view()),

    # Custom actions
    path('api/visualize_geo_data/', visualize_geo_data),
    path('api/geofeature_list_view/', geofeature_list_view),
    path('api/boundingboxfilter/', BoundingBoxFilter.as_view()),
    # path('api/edit_feature_object/', edit_feature_object)
]

urlpatterns.extend(router.urls)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
