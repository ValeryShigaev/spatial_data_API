from typing import Dict, List

from django.contrib.gis.geos import GEOSGeometry, MultiPoint, Point

from ..models import ObjectsP


def collect_geojson_features(instance: ObjectsP) -> List[Dict]:
    """
    This function allows to add object attributes and geometry to geojson
    features list

    Parameters:
    :param instance: construction object
    :type instance: ObjectsP
    :rtype: List[Dict]
    """

    feat_list = [
        {
            'type': 'Feature',
            'properties': {
                'id': str(instance.fid),
                'name': str(instance.name),
                'org': str(instance.org),
                'region': str(instance.region),
                'year': instance.year,
            },
            'geometry': {
                'type': 'MultiPoint',
                'coordinates': GEOSGeometry(instance.geom).coords
            }
        }
    ]
    return feat_list


def collect_geojson(data: Dict) -> Dict:
    """
    This function allows to collect features to one geojson

    Parameters:
    :param data: list of features
    :type data: Dict
    :rtype: Dict
    """

    result = {
        'type': 'FeatureCollection',
        'name': 'objects',
        'crs': {'type': 'name', 'properties':
                {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}},
        'features': []
    }
    for lst in data:
        result['features'].append(lst[0])
    return result


def geometry_from_xy(x: float, y: float) -> MultiPoint:
    """
    This function allows to convert x, y decimal coordinates to Geos geometry

    Parameters:
    :param x: WGS-84 N coordinate
    :type x: float
    :param y: WGS-84 E coordinate
    :type y: float
    :rtype: MultiPoint
    """

    return MultiPoint(Point(y, x))
