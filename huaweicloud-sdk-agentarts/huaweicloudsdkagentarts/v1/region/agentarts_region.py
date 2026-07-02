# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class AgentArtsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("AGENTARTS")

    CN_EAST_4 = Region("cn-east-4",
                        "https://agentarts.cn-east-4.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://agentarts.cn-southwest-2.myhuaweicloud.com")

    static_fields = {
        "cn-east-4": CN_EAST_4,
        "cn-southwest-2": CN_SOUTHWEST_2,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'AgentArts': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
