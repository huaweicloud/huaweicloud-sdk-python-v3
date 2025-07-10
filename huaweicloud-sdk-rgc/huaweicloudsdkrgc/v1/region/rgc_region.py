# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class RgcRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("RGC")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://rgc.cn-north-4.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://rgc.cn-east-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://rgc.cn-south-1.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://rgc.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://rgc.ap-southeast-2.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://rgc.ap-southeast-3.myhuaweicloud.com")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://rgc.ap-southeast-4.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://rgc.af-south-1.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://rgc.la-south-2.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://rgc.la-north-2.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://rgc.sa-brazil-1.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "af-south-1": AF_SOUTH_1,
        "la-south-2": LA_SOUTH_2,
        "la-north-2": LA_NORTH_2,
        "sa-brazil-1": SA_BRAZIL_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Rgc': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
