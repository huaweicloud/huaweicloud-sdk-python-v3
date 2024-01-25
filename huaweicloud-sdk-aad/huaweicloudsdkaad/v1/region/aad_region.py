# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class AadRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("AAD")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://aad.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://aad.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "ap-southeast-1": AP_SOUTHEAST_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Aad': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
