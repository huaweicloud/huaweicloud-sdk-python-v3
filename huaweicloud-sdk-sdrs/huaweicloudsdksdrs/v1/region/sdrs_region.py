# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class SdrsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("SDRS")

    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://sdrs.ap-southeast-3.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://sdrs.cn-north-4.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://sdrs.ap-southeast-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://sdrs.cn-south-1.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://sdrs.cn-east-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://sdrs.cn-east-3.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://sdrs.af-south-1.myhuaweicloud.com")

    static_fields = {
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-north-4": CN_NORTH_4,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "af-south-1": AF_SOUTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Sdrs': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
