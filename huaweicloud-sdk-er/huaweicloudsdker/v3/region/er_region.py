# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class ErRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("ER")


    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://er.cn-south-1.myhuaweicloud.com")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://er.cn-east-3.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://er.cn-north-4.myhuaweicloud.com")

    CN_NORTH_9 = Region(id="cn-north-9", endpoint="https://er.cn-north-9.myhuaweicloud.com")

    AP_SOUTHEAST_2 = Region(id="ap-southeast-2", endpoint="https://er.ap-southeast-2.myhuaweicloud.com")

    static_fields = {
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-north-4": CN_NORTH_4,
        "cn-north-9": CN_NORTH_9,
        "ap-southeast-2": AP_SOUTHEAST_2,
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


