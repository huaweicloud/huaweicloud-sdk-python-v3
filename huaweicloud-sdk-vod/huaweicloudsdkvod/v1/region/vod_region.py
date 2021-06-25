# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region


class VodRegion:
    def __init__(self):
        pass

    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://vod.cn-east-2.myhuaweicloud.com")

    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://vod.cn-north-1.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://vod.cn-north-4.myhuaweicloud.com")

    static_fields = {
        "cn-east-2": CN_EAST_2,
        "cn-north-1": CN_NORTH_1,
        "cn-north-4": CN_NORTH_4,
    }

    @staticmethod
    def value_of(region_id, static_fields=types.MappingProxyType(static_fields) if six.PY3 else static_fields):
        if region_id is None or len(region_id) == 0:
            raise KeyError("Unexpected empty parameter: region_id.")
        if not static_fields.get(region_id):
            raise KeyError("Unexpected region_id: " + region_id)
        return static_fields.get(region_id)


