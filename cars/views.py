from rest_framework import viewsets
from cars.models import Brand, Car
from cars.serializers import BrandModelSerializer, CarModelSerializer
from dj_rql.drf import RQLFilterBackend
from cars.filters import BrandFilterClass, CarFilterClass


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = BrandFilterClass


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CarFilterClass
