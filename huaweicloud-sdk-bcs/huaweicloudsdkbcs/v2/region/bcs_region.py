# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class BcsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("BCS")

    CN_NORTH_1 = Region("cn-north-1",
                        "https://bcs.cn-north-1.myhuaweicloud.com",
                        "https://bcs.cn-north-1.myhuaweicloud.cn")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://bcs.cn-north-4.myhuaweicloud.com",
                        "https://bcs.cn-north-4.myhuaweicloud.cn")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://bcs.cn-south-1.myhuaweicloud.com",
                        "https://bcs.cn-south-1.myhuaweicloud.cn")
    CN_EAST_2 = Region("cn-east-2",
                        "https://bcs.cn-east-2.myhuaweicloud.com",
                        "https://bcs.cn-east-2.myhuaweicloud.cn")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://bcs.ap-southeast-1.myhuaweicloud.com",
                        "https://bcs.ap-southeast-1.myhuaweicloud.cn")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://bcs.ap-southeast-2.myhuaweicloud.com",
                        "https://bcs.ap-southeast-2.myhuaweicloud.cn")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://bcs.ap-southeast-3.myhuaweicloud.com",
                        "https://bcs.ap-southeast-3.myhuaweicloud.cn")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://bcs.ap-southeast-4.myhuaweicloud.com",
                        "https://bcs.ap-southeast-4.myhuaweicloud.cn")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-2": CN_EAST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-4": AP_SOUTHEAST_4,
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


