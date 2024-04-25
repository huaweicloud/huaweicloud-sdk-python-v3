# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class StsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("STS")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://sts.cn-north-4.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://sts.cn-south-1.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://sts.cn-east-3.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://sts.cn-southwest-2.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://sts.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://sts.ap-southeast-3.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://sts.ap-southeast-2.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://sts.sa-brazil-1.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://sts.la-south-2.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://sts.af-south-1.myhuaweicloud.com")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://sts.ap-southeast-4.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://sts.tr-west-1.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-south-2": LA_SOUTH_2,
        "af-south-1": AF_SOUTH_1,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "tr-west-1": TR_WEST_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Sts': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
