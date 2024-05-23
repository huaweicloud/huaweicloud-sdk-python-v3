# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class ErRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("ER")

    CN_SOUTH_1 = Region("cn-south-1",
                        "https://er.cn-south-1.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://er.cn-east-3.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://er.cn-north-4.myhuaweicloud.com")
    CN_NORTH_2 = Region("cn-north-2",
                        "https://er.cn-north-2.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://er.cn-north-9.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://er.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://er.ap-southeast-2.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://er.ap-southeast-3.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://er.cn-southwest-2.myhuaweicloud.com")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://er.ap-southeast-4.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://er.sa-brazil-1.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://er.la-south-2.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://er.tr-west-1.myhuaweicloud.com")
    ME_EAST_1 = Region("me-east-1",
                        "https://er.me-east-1.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://er.af-south-1.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://er.la-north-2.myhuaweicloud.com")
    AE_AD_1 = Region("ae-ad-1",
                        "https://er.ae-ad-1.myhuaweicloud.com")
    AF_NORTH_1 = Region("af-north-1",
                        "https://er.af-north-1.myhuaweicloud.com")

    static_fields = {
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-north-4": CN_NORTH_4,
        "cn-north-2": CN_NORTH_2,
        "cn-north-9": CN_NORTH_9,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-south-2": LA_SOUTH_2,
        "tr-west-1": TR_WEST_1,
        "me-east-1": ME_EAST_1,
        "af-south-1": AF_SOUTH_1,
        "la-north-2": LA_NORTH_2,
        "ae-ad-1": AE_AD_1,
        "af-north-1": AF_NORTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Er': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
