# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class IoTDARegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("IOTDA")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://iotda.cn-north-4.myhuaweicloud.com")
    CN_SOUTH_4 = Region("cn-south-4",
                        "https://iotda.cn-south-4.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://iotda.cn-south-1.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://iotda.cn-east-3.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://iotda.ap-southeast-3.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://iotda.ap-southeast-2.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://iotda.ap-southeast-1.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://iotda.af-south-1.myhuaweicloud.com")
    ME_EAST_1 = Region("me-east-1",
                        "https://iotda.me-east-1.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-south-4": CN_SOUTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "af-south-1": AF_SOUTH_1,
        "me-east-1": ME_EAST_1,
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


