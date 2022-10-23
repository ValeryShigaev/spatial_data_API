import django_filters

from .models import ObjectsP


class ObjectsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    fid = django_filters.NumberFilter()
    org = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ObjectsP
        fields = ("fid", "name", "org", "region", "year", )
