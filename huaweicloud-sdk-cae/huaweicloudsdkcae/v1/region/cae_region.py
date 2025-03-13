# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CaeRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CAE")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://cae.cn-north-4.myhuaweicloud.com",
                        "https://cae.cn-north-4.myhuaweicloud.cn")
    CN_EAST_3 = Region("cn-east-3",
                        "https://cae.cn-east-3.myhuaweicloud.com",
                        "https://cae.cn-east-3.myhuaweicloud.cn")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://cae.cn-south-1.myhuaweicloud.com",
                        "https://cae.cn-south-1.myhuaweicloud.cn")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://cae.ap-southeast-3.myhuaweicloud.com",
                        "https://cae.ap-southeast-3.myhuaweicloud.cn")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://cae.af-south-1.myhuaweicloud.com",
                        "https://cae.af-south-1.myhuaweicloud.cn")
    ME_EAST_1 = Region("me-east-1",
                        "https://cae.me-east-1.myhuaweicloud.com",
                        "https://cae.me-east-1.myhuaweicloud.cn")
    LA_NORTH_2 = Region("la-north-2",
                        "https://cae.la-north-2.myhuaweicloud.com",
                        "https://cae.la-north-2.myhuaweicloud.cn")
    TR_WEST_1 = Region("tr-west-1",
                        "https://cae.tr-west-1.myhuaweicloud.com",
                        "https://cae.tr-west-1.myhuaweicloud.cn")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "af-south-1": AF_SOUTH_1,
        "me-east-1": ME_EAST_1,
        "la-north-2": LA_NORTH_2,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Cae': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
