# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CloudtestRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CLOUDTEST")

    CN_NORTH_1 = Region("cn-north-1",
                        "https://cloudtest-ext.cn-north-1.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://cloudtest-ext.cn-north-4.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://cloudtest-ext.cn-south-1.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://cloudtest-ext.cn-east-2.myhuaweicloud.cn")
    CN_EAST_3 = Region("cn-east-3",
                        "https://cloudtest-ext.cn-east-3.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://cloudtest-ext.la-north-2.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://cloudtest-ext.sa-brazil-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://cloudtest-ext.ap-southeast-3.myhuaweicloud.com")

    static_fields = {
        "cn-north-1": CN_NORTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "la-north-2": LA_NORTH_2,
        "sa-brazil-1": SA_BRAZIL_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Cloudtest': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
