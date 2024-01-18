# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CodeArtsCheckRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CODEARTSCHECK")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://codearts-check.cn-north-4.myhuaweicloud.com",
                        "https://codearts-check.cn-north-4.myhuaweicloud.cn")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://codearts-check.cn-north-1.myhuaweicloud.com",
                        "https://codearts-check.cn-north-1.myhuaweicloud.cn")
    CN_EAST_2 = Region("cn-east-2",
                        "https://codearts-check.cn-east-2.myhuaweicloud.com",
                        "https://codearts-check.cn-east-2.myhuaweicloud.cn")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://codearts-check.cn-south-1.myhuaweicloud.com",
                        "https://codearts-check.cn-south-1.myhuaweicloud.cn")
    CN_EAST_3 = Region("cn-east-3",
                        "https://codearts-check.cn-east-3.myhuaweicloud.com",
                        "https://codearts-check.cn-east-3.myhuaweicloud.cn")
    LA_NORTH_2 = Region("la-north-2",
                        "https://codearts-check.la-north-2.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://codearts-check.sa-brazil-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://codearts-check.ap-southeast-3.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-east-2": CN_EAST_2,
        "cn-south-1": CN_SOUTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'CodeArtsCheck': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
