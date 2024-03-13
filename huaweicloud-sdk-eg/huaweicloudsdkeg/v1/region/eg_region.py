# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class EgRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("EG")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://eg.cn-north-4.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://eg.cn-east-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://eg.cn-east-3.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
    }

    @classmethod
    def value_of(cls, region_id, static_fields=None):
        if not region_id:
            raise KeyError("Unexpected empty parameter: region_id")

        fields = static_fields or cls.static_fields

        region = cls._PROVIDER.get_region(region_id)
        if region:
            return region

        if region_id in fields:
            return fields.get(region_id)

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Eg': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
