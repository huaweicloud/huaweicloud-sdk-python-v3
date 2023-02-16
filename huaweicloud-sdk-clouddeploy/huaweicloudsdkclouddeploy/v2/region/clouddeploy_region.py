# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CloudDeployRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CLOUDDEPLOY")

    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://clouddeploy.ap-southeast-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://clouddeploy.cn-south-1.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://clouddeploy.cn-east-3.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://clouddeploy.cn-east-2.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://clouddeploy.cn-north-4.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://clouddeploy.sa-brazil-1.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://clouddeploy.la-north-2.myhuaweicloud.com")

    static_fields = {
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-east-2": CN_EAST_2,
        "cn-north-4": CN_NORTH_4,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-north-2": LA_NORTH_2,
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


