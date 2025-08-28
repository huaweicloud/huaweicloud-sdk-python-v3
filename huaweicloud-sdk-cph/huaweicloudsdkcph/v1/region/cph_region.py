# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CphRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CPH")

    RU_NORTHWEST_2 = Region("ru-northwest-2",
                        "https://cph.ru-northwest-2.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://cph.ap-southeast-3.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://cph.ap-southeast-1.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://cph.cn-north-4.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://cph.cn-south-1.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://cph.cn-southwest-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://cph.cn-east-3.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://cph.cn-east-2.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://cph.cn-north-9.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://cph.la-south-2.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://cph.la-north-2.myhuaweicloud.com")
    AF_NORTH_1 = Region("af-north-1",
                        "https://cph.af-north-1.myhuaweicloud.com")
    CN_EAST_4 = Region("cn-east-4",
                        "https://cph.cn-east-4.myhuaweicloud.com")

    static_fields = {
        "ru-northwest-2": RU_NORTHWEST_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "cn-east-3": CN_EAST_3,
        "cn-east-2": CN_EAST_2,
        "cn-north-9": CN_NORTH_9,
        "la-south-2": LA_SOUTH_2,
        "la-north-2": LA_NORTH_2,
        "af-north-1": AF_NORTH_1,
        "cn-east-4": CN_EAST_4,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Cph': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
