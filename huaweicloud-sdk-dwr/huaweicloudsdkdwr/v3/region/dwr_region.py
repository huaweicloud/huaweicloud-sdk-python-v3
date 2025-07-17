# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class DwrRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("DWR")

    CN_SOUTH_1 = Region("cn-south-1",
                        "https://dwr.cn-south-1.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://dwr-lms.cn-southwest-2.myhuaweicloud.com")
    CN_NORTH_11 = Region("cn-north-11",
                        "https://dwr-lms.cn-north-11.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://dwr-lms.cn-north-9.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://dwr-lms.cn-east-3.myhuaweicloud.com")

    static_fields = {
        "cn-south-1": CN_SOUTH_1,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "cn-north-11": CN_NORTH_11,
        "cn-north-9": CN_NORTH_9,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Dwr': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
