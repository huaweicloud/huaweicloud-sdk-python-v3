# coding: utf-8

import types

from huaweicloudsdkcore.region.region import Region


class CceRegion:
    def __init__(self):
        pass

    CN_NORTH_2 = Region(id="cn-north-2", endpoint="https://cce.cn-north-2.myhuaweicloud.com")

    static_fields = types.MappingProxyType({
        "cn-north-2": CN_NORTH_2,
    })

    @staticmethod
    def value_of(region_id, static_fields=static_fields):
        if region_id is None or len(region_id) == 0:
            raise KeyError("Unexpected empty parameter: region_id.")
        if not static_fields.get(region_id):
            raise KeyError("Unexpected region_id: " + region_id)
        return static_fields.get(region_id)


