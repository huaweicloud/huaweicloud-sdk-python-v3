# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class EvsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("EVS")

    EU_WEST_101 = Region("eu-west-101",
                        "https://evs.eu-west-101.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://evs.af-south-1.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://evs.cn-north-4.myhuaweicloud.com")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://evs.cn-north-1.myhuaweicloud.com")
    CN_NORTH_2 = Region("cn-north-2",
                        "https://evs.cn-north-2.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://evs.cn-east-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://evs.cn-east-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://evs.cn-south-1.myhuaweicloud.com")
    CN_SOUTH_2 = Region("cn-south-2",
                        "https://evs.cn-south-2.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://evs.cn-southwest-2.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://evs.ap-southeast-2.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://evs.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://evs.ap-southeast-3.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://evs.sa-brazil-1.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://evs.la-north-2.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://evs.la-south-2.myhuaweicloud.com")
    NA_MEXICO_1 = Region("na-mexico-1",
                        "https://evs.na-mexico-1.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://evs.cn-north-9.myhuaweicloud.com")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://evs.ap-southeast-4.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://evs.tr-west-1.myhuaweicloud.com")
    AE_AD_1 = Region("ae-ad-1",
                        "https://evs.ae-ad-1.myhuaweicloud.com")
    ME_EAST_1 = Region("me-east-1",
                        "https://evs.me-east-1.myhuaweicloud.com")
    EU_WEST_0 = Region("eu-west-0",
                        "https://evs.eu-west-0.myhuaweicloud.com")
    CN_SOUTH_4 = Region("cn-south-4",
                        "https://evs.cn-south-4.myhuaweicloud.com")
    RU_MOSCOW_1 = Region("ru-moscow-1",
                        "https://evs.ru-moscow-1.myhuaweicloud.com")
    MY_KUALALUMPUR_1 = Region("my-kualalumpur-1",
                        "https://evs.my-kualalumpur-1.myhuaweicloud.com")
    CN_EAST_4 = Region("cn-east-4",
                        "https://evs.cn-east-4.myhuaweicloud.com")
    CN_EAST_5 = Region("cn-east-5",
                        "https://evs.cn-east-5.myhuaweicloud.com")
    CN_NORTH_11 = Region("cn-north-11",
                        "https://evs.cn-north-11.myhuaweicloud.com")
    RU_NORTHWEST_2 = Region("ru-northwest-2",
                        "https://evs.ru-northwest-2.myhuaweicloud.com")
    AF_NORTH_1 = Region("af-north-1",
                        "https://evs.af-north-1.myhuaweicloud.com")
    AP_SOUTHEAST_5 = Region("ap-southeast-5",
                        "https://evs.ap-southeast-5.myhuaweicloud.com")
    CN_NORTH_12 = Region("cn-north-12",
                        "https://evs.cn-north-12.myhuaweicloud.com")

    static_fields = {
        "eu-west-101": EU_WEST_101,
        "af-south-1": AF_SOUTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-north-2": CN_NORTH_2,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "cn-south-2": CN_SOUTH_2,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-north-2": LA_NORTH_2,
        "la-south-2": LA_SOUTH_2,
        "na-mexico-1": NA_MEXICO_1,
        "cn-north-9": CN_NORTH_9,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "tr-west-1": TR_WEST_1,
        "ae-ad-1": AE_AD_1,
        "me-east-1": ME_EAST_1,
        "eu-west-0": EU_WEST_0,
        "cn-south-4": CN_SOUTH_4,
        "ru-moscow-1": RU_MOSCOW_1,
        "my-kualalumpur-1": MY_KUALALUMPUR_1,
        "cn-east-4": CN_EAST_4,
        "cn-east-5": CN_EAST_5,
        "cn-north-11": CN_NORTH_11,
        "ru-northwest-2": RU_NORTHWEST_2,
        "af-north-1": AF_NORTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Evs': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
