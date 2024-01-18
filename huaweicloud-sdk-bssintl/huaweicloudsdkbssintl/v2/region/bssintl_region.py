# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class BssintlRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("BSSINTL")

    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://bss-intl.myhuaweicloud.com")

    static_fields = {
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Bssintl': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
