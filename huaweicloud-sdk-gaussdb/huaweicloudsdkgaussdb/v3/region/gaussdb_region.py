# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class GaussDBRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("GAUSSDB")


    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://gaussdb.cn-north-4.myhuaweicloud.com")

    CN_SOUTHWEST_2 = Region(id="cn-southwest-2", endpoint="https://gaussdb.cn-southwest-2.myhuaweicloud.com")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://gaussdb.cn-east-3.myhuaweicloud.com")

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://gaussdb.cn-south-1.myhuaweicloud.com")

    RU_NORTHWEST_2 = Region(id="ru-northwest-2", endpoint="https://gaussdb.ru-northwest-2.myhuaweicloud.com")

    AP_SOUTHEAST_3 = Region(id="ap-southeast-3", endpoint="https://gaussdb.ap-southeast-3.myhuaweicloud.com")

    CN_NORTH_2 = Region(id="cn-north-2", endpoint="https://gaussdb.cn-north-2.myhuaweicloud.com")

    CN_NORTH_9 = Region(id="cn-north-9", endpoint="https://gaussdb.cn-north-9.myhuaweicloud.com")

    SA_BRAZIL_1 = Region(id="sa-brazil-1", endpoint="https://gaussdb.sa-brazil-1.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "ru-northwest-2": RU_NORTHWEST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-north-2": CN_NORTH_2,
        "cn-north-9": CN_NORTH_9,
        "sa-brazil-1": SA_BRAZIL_1,
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


