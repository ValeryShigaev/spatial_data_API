from rest_framework import serializers

from .models import ObjectsP
from .utils.utils import collect_geojson_features, geometry_from_xy


class ObjectsListSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):

        return collect_geojson_features(instance)

    class Meta:
        model = ObjectsP
        fields = ('fid', 'name', 'region', 'org', 'year',)


class ObjectsCreateSerializer(serializers.ModelSerializer):
    x = serializers.FloatField(required=True, write_only=True,
                               help_text="float: WGS-84 N coordinate")
    y = serializers.FloatField(required=True, write_only=True,
                               help_text="float: WGS-84 E coordinate")

    class Meta:
        model = ObjectsP
        fields = ('name', 'region', 'org', 'year', 'x', 'y')


class ObjectsUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ObjectsP
        fields = ('fid', 'name', 'region', 'org', 'year')


class ObjectsMoveSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = ObjectsP
        fields = ('fid', )