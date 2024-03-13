# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class OctopusRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("OCTOPUS")

    CN_NORTH_11 = Region("cn-north-11",
                        "https://octopus.cn-north-11.myhuaweicloud.com")

    static_fields = {
        "cn-north-11": CN_NORTH_11,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Octopus': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
