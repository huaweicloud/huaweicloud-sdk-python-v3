# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class SFSTurboRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("SFSTURBO")

    EU_WEST_101 = Region("eu-west-101",
                        "https://sfs-turbo.eu-west-101.myhuaweicloud.eu")
    CN_EAST_2 = Region("cn-east-2",
                        "https://sfs-turbo.cn-east-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://sfs-turbo.cn-east-3.myhuaweicloud.com")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://sfs-turbo.cn-north-1.myhuaweicloud.com")
    CN_NORTH_2 = Region("cn-north-2",
                        "https://sfs-turbo.cn-north-2.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://sfs-turbo.cn-north-4.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://sfs-turbo.cn-north-9.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://sfs-turbo.cn-south-1.myhuaweicloud.com")
    CN_SOUTH_2 = Region("cn-south-2",
                        "https://sfs-turbo.cn-south-2.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://sfs-turbo.cn-southwest-2.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://sfs-turbo.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://sfs-turbo.ap-southeast-2.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://sfs-turbo.ap-southeast-3.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://sfs-turbo.sa-brazil-1.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://sfs-turbo.la-south-2.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://sfs-turbo.la-north-2.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://sfs-turbo.af-south-1.myhuaweicloud.com")
    NA_MEXICO_1 = Region("na-mexico-1",
                        "https://sfs-turbo.na-mexico-1.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://sfs-turbo.tr-west-1.myhuaweicloud.com")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://sfs-turbo.ap-southeast-4.myhuaweicloud.com")
    ME_EAST_1 = Region("me-east-1",
                        "https://sfs-turbo.me-east-1.myhuaweicloud.com")
    CN_EAST_5 = Region("cn-east-5",
                        "https://sfs-turbo.cn-east-5.myhuaweicloud.com")
    CN_SOUTH_4 = Region("cn-south-4",
                        "https://sfs-turbo.cn-south-4.myhuaweicloud.com")
    RU_MOSCOW_1 = Region("ru-moscow-1",
                        "https://sfs-turbo.ru-moscow-1.myhuaweicloud.com")
    MY_KUALALUMPUR_1 = Region("my-kualalumpur-1",
                        "https://sfs-turbo.my-kualalumpur-1.myhuaweicloud.com")
    CN_EAST_4 = Region("cn-east-4",
                        "https://sfs-turbo.cn-east-4.myhuaweicloud.com")
    AE_AD_1 = Region("ae-ad-1",
                        "https://sfs-turbo.ae-ad-1.myhuaweicloud.com")
    CN_NORTH_11 = Region("cn-north-11",
                        "https://sfs-turbo.cn-north-11.myhuaweicloud.com")
    AF_NORTH_1 = Region("af-north-1",
                        "https://sfs-turbo.af-north-1.myhuaweicloud.com")
    CN_NORTH_12 = Region("cn-north-12",
                        "https://sfs-turbo.cn-north-12.myhuaweicloud.com")

    static_fields = {
        "eu-west-101": EU_WEST_101,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "cn-north-1": CN_NORTH_1,
        "cn-north-2": CN_NORTH_2,
        "cn-north-4": CN_NORTH_4,
        "cn-north-9": CN_NORTH_9,
        "cn-south-1": CN_SOUTH_1,
        "cn-south-2": CN_SOUTH_2,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-south-2": LA_SOUTH_2,
        "la-north-2": LA_NORTH_2,
        "af-south-1": AF_SOUTH_1,
        "na-mexico-1": NA_MEXICO_1,
        "tr-west-1": TR_WEST_1,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "me-east-1": ME_EAST_1,
        "cn-east-5": CN_EAST_5,
        "cn-south-4": CN_SOUTH_4,
        "ru-moscow-1": RU_MOSCOW_1,
        "my-kualalumpur-1": MY_KUALALUMPUR_1,
        "cn-east-4": CN_EAST_4,
        "ae-ad-1": AE_AD_1,
        "cn-north-11": CN_NORTH_11,
        "af-north-1": AF_NORTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'SFSTurbo': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
