# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class EpsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("EPS")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://eps.myhuaweicloud.com")
    EU_WEST_101 = Region("eu-west-101",
                        "https://eps.eu-west-101.myhuaweicloud.eu")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "eu-west-101": EU_WEST_101,
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


