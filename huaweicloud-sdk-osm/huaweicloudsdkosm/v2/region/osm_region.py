# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region


class OsmRegion:
    def __init__(self):
        pass

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://osm.cn-south-1.myhuaweicloud.cn")

    static_fields = {
        "cn-south-1": CN_SOUTH_1,
    }

    @staticmethod
    def value_of(region_id, static_fields=types.MappingProxyType(static_fields) if six.PY3 else static_fields):
        if region_id is None or len(region_id) == 0:
            raise KeyError("Unexpected empty parameter: region_id.")
        if not static_fields.get(region_id):
            raise KeyError("Unexpected region_id: " + region_id)
        return static_fields.get(region_id)


