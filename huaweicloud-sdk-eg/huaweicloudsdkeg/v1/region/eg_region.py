# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class EgRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("EG")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://eg.cn-north-4.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://eg.cn-east-2.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://eg.cn-east-3.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://eg.sa-brazil-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://eg.ap-southeast-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://eg.cn-south-1.myhuaweicloud.com")
    CN_NORTH_11 = Region("cn-north-11",
                        "https://eg.cn-north-11.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://eg.cn-north-9.myhuaweicloud.com")
    NA_MEXICO_1 = Region("na-mexico-1",
                        "https://eg.na-mexico-1.myhuaweicloud.com")
    EU_WEST_101 = Region("eu-west-101",
                        "https://eg.eu-west-101.myhuaweicloud.eu")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "sa-brazil-1": SA_BRAZIL_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-south-1": CN_SOUTH_1,
        "cn-north-11": CN_NORTH_11,
        "cn-north-9": CN_NORTH_9,
        "na-mexico-1": NA_MEXICO_1,
        "eu-west-101": EU_WEST_101,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Eg': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
