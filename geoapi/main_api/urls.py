from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from .views import (ObjectsCreate, ObjectsDelete, ObjectsList, ObjectsMove,
                    ObjectsUpdate)

urlpatterns = [
    path('', include_docs_urls(title="Argo spatial data API"),
         name='main'),
    path('objects/', ObjectsList.as_view(), name='objects_list'),
    path('objects/create', ObjectsCreate.as_view(), name='objects_create'),
    path('objects/update/<int:fid>', ObjectsUpdate.as_view(lookup_field="fid"),
         name='objects_update'),
    path('objects/move/<int:fid>', ObjectsMove.as_view(lookup_field="fid"),
         name='objects_move'),
    path('objects/delete/<int:fid>', ObjectsDelete.as_view(lookup_field="fid"),
         name='objects_delete'),
]