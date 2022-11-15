from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .filters import ObjectsFilter
from .models import ObjectsP
from .serializers import (ObjectsCreateSerializer, ObjectsDeleteSerializer,
                          ObjectsListSerializer, ObjectsMoveSerializer,
                          ObjectsUpdateSerializer)
from .utils.utils import collect_geojson, geometry_from_xy


class ObjectsList(generics.ListAPIView):
    """ Returns a list of constructions objects """

    permission_classes = [IsAuthenticated, ]
    serializer_class = ObjectsListSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = ObjectsFilter
    queryset = ObjectsP.objects.all()


class ObjectsCreate(generics.CreateAPIView):
    """ Uses for creating construction objects """

    permission_classes = (IsAuthenticated,)
    serializer_class = ObjectsCreateSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        x, y = data.get('x'), data.get('y')
        serializer.validated_data.pop('x', None)
        serializer.validated_data.pop('y', None)
        serializer.save(geom=geometry_from_xy(x, y))


class ObjectsUpdate(generics.UpdateAPIView):
    """ Updates attributes of construction object """

    permission_classes = (IsAuthenticated,)
    serializer_class = ObjectsUpdateSerializer
    queryset = ObjectsP.objects.all()


class ObjectsMove(generics.UpdateAPIView):
    """ Changes construction objects geometry """

    permission_classes = (IsAuthenticated,)
    serializer_class = ObjectsMoveSerializer
    queryset = ObjectsP.objects.all()


class ObjectsDelete(generics.DestroyAPIView):
    """ Allows you to delete construction object """

    permission_classes = (IsAuthenticated,)
    serializer_class = ObjectsDeleteSerializer
    queryset = ObjectsP.objects.all()
