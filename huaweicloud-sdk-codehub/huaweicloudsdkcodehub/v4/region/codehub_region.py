# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CodeHubRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CODEHUB")

    CN_EAST_2 = Region("cn-east-2",
                        "https://codehub-ext.cn-east-2.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://codehub-ext.cn-south-1.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://codehub-ext.cn-east-3.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://codehub-ext.cn-north-4.myhuaweicloud.com")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://codehub-ext.cn-north-1.myhuaweicloud.com")
    CN_SOUTH_2 = Region("cn-south-2",
                        "https://codehub-ext.cn-south-2.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://codehub-ext.cn-southwest-2.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://codehub-ext.sa-brazil-1.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://codehub-ext.la-north-2.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://codehub-ext.ap-southeast-3.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://codeartsrepo-ext.la-south-2.myhuaweicloud.com")
    ME_EAST_1 = Region("me-east-1",
                        "https://repo.me-east-1.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://codeartsrepo-ext.tr-west-1.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://repo.af-south-1.myhuaweicloud.com")
    AF_NORTH_1 = Region("af-north-1",
                        "https://repo.af-north-1.myhuaweicloud.com")

    static_fields = {
        "cn-east-2": CN_EAST_2,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-south-2": CN_SOUTH_2,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-north-2": LA_NORTH_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "la-south-2": LA_SOUTH_2,
        "me-east-1": ME_EAST_1,
        "tr-west-1": TR_WEST_1,
        "af-south-1": AF_SOUTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'CodeHub': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
