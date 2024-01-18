# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CgsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CGS")

    CN_SOUTH_4 = Region("cn-south-4",
                        "https://cgs.cn-south-4.myhuaweicloud.com")
    AE_AD_1 = Region("ae-ad-1",
                        "https://cgs.ae-ad-1.myhuaweicloud.com")

    static_fields = {
        "cn-south-4": CN_SOUTH_4,
        "ae-ad-1": AE_AD_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Cgs': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
