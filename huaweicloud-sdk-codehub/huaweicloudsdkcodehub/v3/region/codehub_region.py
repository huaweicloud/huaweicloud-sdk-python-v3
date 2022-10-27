# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CodeHubRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CODEHUB")


    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://codehub-ext.cn-east-2.myhuaweicloud.com")

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://codehub-ext.cn-south-1.myhuaweicloud.com")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://codehub-ext.cn-east-3.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://codehub-ext.cn-north-4.myhuaweicloud.com")

    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://codehub-ext.cn-north-1.myhuaweicloud.com")

    CN_SOUTH_2 = Region(id="cn-south-2", endpoint="https://codehub-ext.cn-south-2.myhuaweicloud.com")

    CN_SOUTHWEST_2 = Region(id="cn-southwest-2", endpoint="https://codehub-ext.cn-southwest-2.myhuaweicloud.com")

    SA_BRAZIL_1 = Region(id="sa-brazil-1", endpoint="https://codehub-ext.sa-brazil-1.myhuaweicloud.com")

    LA_NORTH_2 = Region(id="la-north-2", endpoint="https://codehub-ext.la-north-2.myhuaweicloud.com")

    static_fields = {
        "cn-east-2": CN_EAST_2,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-south-2": CN_SOUTH_2,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-north-2": LA_NORTH_2,
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


