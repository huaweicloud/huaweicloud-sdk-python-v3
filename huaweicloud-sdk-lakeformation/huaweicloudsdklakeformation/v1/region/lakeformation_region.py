# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class LakeFormationRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("LAKEFORMATION")


    CN_NORTH_9 = Region(id="cn-north-9", endpoint="https://lakeformation.cn-north-9.myhuaweicloud.com")

    CN_NORTH_2 = Region(id="cn-north-2", endpoint="https://lakeformation.cn-north-2.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://lakeformation.cn-north-4.myhuaweicloud.com")

    static_fields = {
        "cn-north-9": CN_NORTH_9,
        "cn-north-2": CN_NORTH_2,
        "cn-north-4": CN_NORTH_4,
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


