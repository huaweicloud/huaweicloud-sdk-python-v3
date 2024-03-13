# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class IdmeRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("IDME")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://dme.cn-north-4.myhuaweicloud.com")
    CN_SOUTH_4 = Region("cn-south-4",
                        "https://dme.cn-south-4.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-south-4": CN_SOUTH_4,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Idme': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
