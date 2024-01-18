# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class BssRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("BSS")

    CN_NORTH_1 = Region("cn-north-1",
                        "https://bss.myhuaweicloud.com")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Bss': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
