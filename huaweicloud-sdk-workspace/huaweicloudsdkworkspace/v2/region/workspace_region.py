# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class WorkspaceRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("WORKSPACE")

    CN_EAST_3 = Region("cn-east-3",
                        "https://workspace.cn-east-3.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://workspace.cn-north-4.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://workspace.cn-south-1.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://workspace.cn-southwest-2.myhuaweicloud.com")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://workspace.la-south-2.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://workspace.sa-brazil-1.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://workspace.la-north-2.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://workspace.ap-southeast-3.myhuaweicloud.com")
    CN_NORTH_9 = Region("cn-north-9",
                        "https://workspace.cn-north-9.myhuaweicloud.com")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://workspace.ap-southeast-1.myhuaweicloud.com")
    CN_EAST_5 = Region("cn-east-5",
                        "https://workspace.cn-east-5.myhuaweicloud.com")
    ME_EAST_1 = Region("me-east-1",
                        "https://workspace.me-east-1.myhuaweicloud.com")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://workspace.af-south-1.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://workspace.tr-west-1.myhuaweicloud.com")
    CN_NORTH_11 = Region("cn-north-11",
                        "https://workspace.cn-north-11.myhuaweicloud.com")
    AF_NORTH_1 = Region("af-north-1",
                        "https://workspace.af-north-1.myhuaweicloud.com")

    static_fields = {
        "cn-east-3": CN_EAST_3,
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "la-south-2": LA_SOUTH_2,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-north-2": LA_NORTH_2,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-north-9": CN_NORTH_9,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "cn-east-5": CN_EAST_5,
        "me-east-1": ME_EAST_1,
        "af-south-1": AF_SOUTH_1,
        "tr-west-1": TR_WEST_1,
        "cn-north-11": CN_NORTH_11,
        "af-north-1": AF_NORTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Workspace': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
