# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class OmsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("OMS")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://oms.cn-north-4.myhuaweicloud.com")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://oms.cn-north-1.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://oms.cn-east-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://oms.cn-east-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://oms.cn-south-1.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://oms.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://oms.ap-southeast-3.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://oms.la-south-2.myhuaweicloud.com")
    CN_SOUTH_4 = Region("cn-south-4",
                        "https://oms.cn-south-4.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://oms.cn-southwest-2.myhuaweicloud.com")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://oms.ap-southeast-4.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://oms.cn-north-9.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://oms.ap-southeast-2.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://oms.la-north-2.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://oms.tr-west-1.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://oms.sa-brazil-1.myhuaweicloud.com")
    ME_EAST_1 = Region("me-east-1",
                        "https://oms.me-east-1.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://oms.af-south-1.myhuaweicloud.com")
    CN_EAST_4 = Region("cn-east-4",
                        "https://oms.cn-east-4.myhuaweicloud.com")
    AP_SOUTHEAST_5 = Region("ap-southeast-5",
                        "https://oms.ap-southeast-5.myhuaweicloud.com")
    CN_NORTH_12 = Region("cn-north-12",
                        "https://oms.cn-north-12.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "la-south-2": LA_SOUTH_2,
        "cn-south-4": CN_SOUTH_4,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "cn-north-9": CN_NORTH_9,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "la-north-2": LA_NORTH_2,
        "tr-west-1": TR_WEST_1,
        "sa-brazil-1": SA_BRAZIL_1,
        "me-east-1": ME_EAST_1,
        "af-south-1": AF_SOUTH_1,
        "cn-east-4": CN_EAST_4,
        "ap-southeast-5": AP_SOUTHEAST_5,
        "cn-north-12": CN_NORTH_12,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Oms': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
