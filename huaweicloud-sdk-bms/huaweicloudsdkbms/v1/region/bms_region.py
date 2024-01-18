# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class BmsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("BMS")

    CN_NORTH_2 = Region("cn-north-2",
                        "https://bms.cn-north-2.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://bms.cn-north-4.myhuaweicloud.com")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://bms.cn-north-1.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://bms.cn-east-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://bms.cn-east-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://bms.cn-south-1.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://bms.ap-southeast-2.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://bms.ap-southeast-3.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://bms.ap-southeast-1.myhuaweicloud.com")
    RU_NORTHWEST_2 = Region("ru-northwest-2",
                        "https://bms.ru-northwest-2.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://bms.la-south-2.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://bms.sa-brazil-1.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://bms.cn-north-9.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://bms.cn-southwest-2.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://bms.af-south-1.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://bms.la-north-2.myhuaweicloud.com")
    CN_SOUTH_2 = Region("cn-south-2",
                        "https://bms.cn-south-2.myhuaweicloud.com")
    NA_MEXICO_1 = Region("na-mexico-1",
                        "https://bms.na-mexico-1.myhuaweicloud.com")

    static_fields = {
        "cn-north-2": CN_NORTH_2,
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ru-northwest-2": RU_NORTHWEST_2,
        "la-south-2": LA_SOUTH_2,
        "sa-brazil-1": SA_BRAZIL_1,
        "cn-north-9": CN_NORTH_9,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "af-south-1": AF_SOUTH_1,
        "la-north-2": LA_NORTH_2,
        "cn-south-2": CN_SOUTH_2,
        "na-mexico-1": NA_MEXICO_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Bms': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
