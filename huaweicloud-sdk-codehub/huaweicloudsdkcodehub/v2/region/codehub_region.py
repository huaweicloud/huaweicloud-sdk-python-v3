# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region


class CodehubRegion:
    def __init__(self):
        pass

    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://codehub-ext.cn-north-1.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://codehub-ext.cn-north-4.myhuaweicloud.com")

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://codehub-ext.cn-south-1.myhuaweicloud.com")

    CN_SOUTH_2 = Region(id="cn-south-2", endpoint="https://codehub-ext.cn-south-2.myhuaweicloud.com")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://codehub-ext.cn-east-3.myhuaweicloud.com")

    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://codehub-ext.cn-east-2.myhuaweicloud.com")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-south-2": CN_SOUTH_2,
        "cn-east-3": CN_EAST_3,
        "cn-east-2": CN_EAST_2,
    }

    @staticmethod
    def value_of(region_id, static_fields=types.MappingProxyType(static_fields) if six.PY3 else static_fields):
        if region_id is None or len(region_id) == 0:
            raise KeyError("Unexpected empty parameter: region_id.")
        if not static_fields.get(region_id):
            raise KeyError("Unexpected region_id: " + region_id)
        return static_fields.get(region_id)


