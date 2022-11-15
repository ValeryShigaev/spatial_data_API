from rest_framework import serializers
from rest_framework_gis import serializers as serializers_geo
from django.contrib.gis.geos import GEOSGeometry, Point

from .models import ObjectsP
from .utils.utils import geometry_from_xy


class ObjectsListSerializer(serializers_geo.GeoFeatureModelSerializer):
    """ Serialized objects features to geojson """

    other_point = serializers_geo.GeometrySerializerMethodField()

    def get_other_point(self, obj):
        print(GEOSGeometry(obj.geom).coords)
        return Point(GEOSGeometry(obj.geom).coords[0])

    class Meta:
        model = ObjectsP
        fields = ('fid', 'name', 'region', 'org', 'year',)
        geo_field = 'other_point'


class ObjectsCreateSerializer(serializers.ModelSerializer):
    """ Creating objects """

    x = serializers.FloatField(required=True, write_only=True,
                               help_text="float: WGS-84 N coordinate")
    y = serializers.FloatField(required=True, write_only=True,
                               help_text="float: WGS-84 E coordinate")

    class Meta:
        model = ObjectsP
        fields = ('name', 'region', 'org', 'year', 'x', 'y')


class ObjectsUpdateSerializer(serializers.ModelSerializer):
    """ Updating objects """

    class Meta:
        model = ObjectsP
        fields = ('fid', 'name', 'region', 'org', 'year')


class ObjectsMoveSerializer(serializers.ModelSerializer):
    """ Updates objects geometry """

    x = serializers.FloatField(required=True, write_only=True,
                               help_text="float: WGS-84 N coordinate")
    y = serializers.FloatField(required=True, write_only=True,
                               help_text="float: WGS-84 E coordinate")

    def update(self, instance, validated_data):
        x, y = validated_data.get('x'), validated_data.get('y')
        validated_data["geom"] = geometry_from_xy(x, y)
        validated_data.pop('x', None)
        validated_data.pop('y', None)
        obj = ObjectsP.objects.get(fid=instance.fid)
        ObjectsP.objects.filter(fid=instance.fid).update(**validated_data)
        return obj

    class Meta:
        model = ObjectsP
        fields = ('fid', 'x', 'y')


class ObjectsDeleteSerializer(serializers.ModelSerializer):
    """ Deleting objects """

    class Meta:
        model = ObjectsP
        fields = ('fid', )
