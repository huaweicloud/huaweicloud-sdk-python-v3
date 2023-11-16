# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class AosRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("AOS")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://aos.cn-north-4.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://aos.cn-south-1.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://aos.cn-east-3.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://aos.cn-north-9.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://aos.cn-southwest-2.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://aos.ap-southeast-3.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://aos.ap-southeast-2.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://aos.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://aos.ap-southeast-4.myhuaweicloud.com")
    ME_EAST_1 = Region("me-east-1",
                        "https://aos.me-east-1.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://aos.tr-west-1.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-north-9": CN_NORTH_9,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "me-east-1": ME_EAST_1,
        "tr-west-1": TR_WEST_1,
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


