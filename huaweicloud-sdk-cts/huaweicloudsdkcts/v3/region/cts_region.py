# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CtsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CTS")

    AF_SOUTH_1 = Region("af-south-1",
                        "https://cts.af-south-1.myhuaweicloud.com",
                        "https://cts.af-south-1.myhuaweicloud.cn")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://cts.cn-north-4.myhuaweicloud.com",
                        "https://cts.cn-north-4.myhuaweicloud.cn")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://cts.cn-north-1.myhuaweicloud.com",
                        "https://cts.cn-north-1.myhuaweicloud.cn")
    CN_EAST_2 = Region("cn-east-2",
                        "https://cts.cn-east-2.myhuaweicloud.com",
                        "https://cts.cn-east-2.myhuaweicloud.cn")
    CN_EAST_3 = Region("cn-east-3",
                        "https://cts.cn-east-3.myhuaweicloud.com",
                        "https://cts.cn-east-3.myhuaweicloud.cn")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://cts.cn-south-1.myhuaweicloud.com",
                        "https://cts.cn-south-1.myhuaweicloud.cn")
    CN_SOUTH_2 = Region("cn-south-2",
                        "https://cts.cn-south-2.myhuaweicloud.com",
                        "https://cts.cn-south-2.myhuaweicloud.cn")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://cts.cn-southwest-2.myhuaweicloud.com",
                        "https://cts.cn-southwest-2.myhuaweicloud.cn")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://cts.ap-southeast-2.myhuaweicloud.com",
                        "https://cts.ap-southeast-2.myhuaweicloud.cn")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://cts.ap-southeast-1.myhuaweicloud.com",
                        "https://cts.ap-southeast-1.myhuaweicloud.cn")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://cts.ap-southeast-3.myhuaweicloud.com",
                        "https://cts.ap-southeast-3.myhuaweicloud.cn")
    CN_NORTH_2 = Region("cn-north-2",
                        "https://cts.cn-north-2.myhuaweicloud.com",
                        "https://cts.cn-north-2.myhuaweicloud.cn")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://cts.cn-north-9.myhuaweicloud.com",
                        "https://cts.cn-north-9.myhuaweicloud.cn")
    CN_SOUTH_4 = Region("cn-south-4",
                        "https://cts.cn-south-4.myhuaweicloud.com",
                        "https://cts.cn-south-4.myhuaweicloud.cn")
    RU_NORTHWEST_2 = Region("ru-northwest-2",
                        "https://cts.ru-northwest-2.myhuaweicloud.com",
                        "https://cts.ru-northwest-2.myhuaweicloud.cn")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://cts.la-south-2.myhuaweicloud.com",
                        "https://cts.la-south-2.myhuaweicloud.cn")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://cts.sa-brazil-1.myhuaweicloud.com",
                        "https://cts.sa-brazil-1.myhuaweicloud.cn")
    LA_NORTH_2 = Region("la-north-2",
                        "https://cts.la-north-2.myhuaweicloud.com",
                        "https://cts.la-north-2.myhuaweicloud.cn")
    NA_MEXICO_1 = Region("na-mexico-1",
                        "https://cts.na-mexico-1.myhuaweicloud.com",
                        "https://cts.na-mexico-1.myhuaweicloud.cn")
    EU_WEST_101 = Region("eu-west-101",
                        "https://cts.eu-west-101.myhuaweicloud.eu")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://cts.ap-southeast-4.myhuaweicloud.com",
                        "https://cts.ap-southeast-4.myhuaweicloud.cn")
    TR_WEST_1 = Region("tr-west-1",
                        "https://cts.tr-west-1.myhuaweicloud.com",
                        "https://cts.tr-west-1.myhuaweicloud.cn")

    static_fields = {
        "af-south-1": AF_SOUTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "cn-south-2": CN_SOUTH_2,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-north-2": CN_NORTH_2,
        "cn-north-9": CN_NORTH_9,
        "cn-south-4": CN_SOUTH_4,
        "ru-northwest-2": RU_NORTHWEST_2,
        "la-south-2": LA_SOUTH_2,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-north-2": LA_NORTH_2,
        "na-mexico-1": NA_MEXICO_1,
        "eu-west-101": EU_WEST_101,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "tr-west-1": TR_WEST_1,
    }

    @classmethod
    def value_of(cls, region_id, static_fields=None):
        if not region_id:
            raise KeyError("Unexpected empty parameter: region_id.")

        fields = static_fields if static_fields else cls.static_fields

        region = cls._PROVIDER.get_region(region_id)
        if region:
            return region

        if region_id in fields:
            return fields.get(region_id)

        raise KeyError("Unexpected region_id: " + region_id)


