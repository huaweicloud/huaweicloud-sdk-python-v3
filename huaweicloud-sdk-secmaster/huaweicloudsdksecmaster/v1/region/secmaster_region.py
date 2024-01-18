# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class SecMasterRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("SECMASTER")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://sa.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://secmaster.cn-east-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://secmaster.cn-south-1.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://secmaster.cn-north-9.myhuaweicloud.com")
    CN_NORTH_2 = Region("cn-north-2",
                        "https://secmaster.cn-north-2.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://secmaster.cn-east-2.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://secmaster.cn-southwest-2.myhuaweicloud.com")
    CN_SOUTH_2 = Region("cn-south-2",
                        "https://secmaster.cn-south-2.myhuaweicloud.com")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://secmaster.cn-north-1.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "cn-north-9": CN_NORTH_9,
        "cn-north-2": CN_NORTH_2,
        "cn-east-2": CN_EAST_2,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "cn-south-2": CN_SOUTH_2,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'SecMaster': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
