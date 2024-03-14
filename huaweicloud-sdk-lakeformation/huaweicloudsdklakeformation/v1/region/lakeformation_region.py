# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class LakeFormationRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("LAKEFORMATION")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://lakeformation.cn-north-4.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://lakeformation.cn-north-9.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://lakeformation.cn-east-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://lakeformation.cn-south-1.myhuaweicloud.com")
    CN_NORTH_11 = Region("cn-north-11",
                        "https://lakeformation.cn-north-11.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://lakeformation.la-north-2.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-north-9": CN_NORTH_9,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "cn-north-11": CN_NORTH_11,
        "la-north-2": LA_NORTH_2,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'LakeFormation': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
