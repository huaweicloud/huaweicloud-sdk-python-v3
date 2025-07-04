# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class TmsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("TMS")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://tms.myhuaweicloud.com",
                        "https://tms.myhuaweicloud.cn")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://tms-intl.myhuaweicloud.com",
                        "https://tms.ap-southeast-1.myhuaweicloud.com",
                        "https://tms.ap-southeast-1.myhuaweicloud.cn")
    EU_WEST_101 = Region("eu-west-101",
                        "https://tms.eu-west-101.myhuaweicloud.eu")
    RU_MOSCOW_1 = Region("ru-moscow-1",
                        "https://tms.ru-moscow-1.myhuaweicloud.com",
                        "https://tms.ru-moscow-1.myhuaweicloud.cn")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "eu-west-101": EU_WEST_101,
        "ru-moscow-1": RU_MOSCOW_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Tms': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
