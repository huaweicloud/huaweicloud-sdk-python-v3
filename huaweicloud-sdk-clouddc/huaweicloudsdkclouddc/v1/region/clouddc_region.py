# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CloudDCRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CLOUDDC")

    CN_EAST_3 = Region("cn-east-3",
                        "https://clouddc.cn-east-3.myhuaweicloud.com")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://clouddc.cn-southwest-2.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://clouddc.cn-south-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://clouddc.ap-southeast-3.myhuaweicloud.com")

    static_fields = {
        "cn-east-3": CN_EAST_3,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "cn-south-1": CN_SOUTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'CloudDC': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
