# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class RomaRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("ROMA")

    CN_NORTH_1 = Region("cn-north-1",
                        "https://roma.cn-north-1.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://roma.cn-north-4.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://roma.cn-east-3.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://roma.cn-east-2.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://roma.cn-south-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://roma.ap-southeast-3.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://roma.ap-southeast-1.myhuaweicloud.com")
    RU_NORTHWEST_2 = Region("ru-northwest-2",
                        "https://roma.ru-northwest-2.myhuaweicloud.com")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-east-3": CN_EAST_3,
        "cn-east-2": CN_EAST_2,
        "cn-south-1": CN_SOUTH_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ru-northwest-2": RU_NORTHWEST_2,
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


