# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class DgcRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("DGC")

    CN_NORTH_1 = Region("cn-north-1",
                        "https://dayu-dlf.cn-north-1.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://dayu-dlf.cn-north-4.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://dayu-dlf.cn-east-3.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://dayu-dlf.cn-east-2.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://dayu-dlf.cn-south-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://dayu-dlf.ap-southeast-3.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://dayu-dlf.ap-southeast-3.myhuaweicloud.com")
    RU_NORTHWEST_2 = Region("ru-northwest-2",
                        "https://dayu-dlf.ru-northwest-2.myhuaweicloud.com")
    CN_NORTH_11 = Region("cn-north-11",
                        "https://dayu-dlf.cn-north-11.myhuaweicloud.com")
    RU_MOSCOW_1 = Region("ru-moscow-1",
                        "https://dayu-dlf.ru-moscow-1.myhuaweicloud.com")
    MY_KUALALUMPUR_1 = Region("my-kualalumpur-1",
                        "https://dayu-dlf.my-kualalumpur-1.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://dayu-dlf.tr-west-1.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://dayu-dlf.cn-north-9.myhuaweicloud.com")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-east-3": CN_EAST_3,
        "cn-east-2": CN_EAST_2,
        "cn-south-1": CN_SOUTH_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ru-northwest-2": RU_NORTHWEST_2,
        "cn-north-11": CN_NORTH_11,
        "ru-moscow-1": RU_MOSCOW_1,
        "my-kualalumpur-1": MY_KUALALUMPUR_1,
        "tr-west-1": TR_WEST_1,
        "cn-north-9": CN_NORTH_9,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Dgc': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
