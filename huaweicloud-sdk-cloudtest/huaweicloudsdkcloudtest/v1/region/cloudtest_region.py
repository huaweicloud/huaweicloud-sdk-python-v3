# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CloudtestRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CLOUDTEST")


    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://cloudtest-ext.cn-north-1.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://cloudtest-ext.cn-north-4.myhuaweicloud.com")

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://cloudtest-ext.cn-south-1.myhuaweicloud.com")

    CN_SOUTH_2 = Region(id="cn-south-2", endpoint="https://cloudtest-ext.cn-south-2.myhuaweicloud.com")

    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://cloudtest-ext.cn-east-2.myhuaweicloud.cn")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://cloudtest-ext.cn-east-3.myhuaweicloud.com")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-south-2": CN_SOUTH_2,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
    }

    @classmethod
    def value_of(cls, region_id, static_fields=None):
        if not region_id:
            raise KeyError("Unexpected empty parameter: region_id.")

        fields = static_fields if static_fields else cls.static_fields

        region = cls._PROVIDER.get_region(region_id)
        if region:
            return region

        if region_id in fields:
            return fields.get(region_id)

        raise KeyError("Unexpected region_id: " + region_id)


