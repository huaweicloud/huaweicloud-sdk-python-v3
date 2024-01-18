# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class ImageRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("IMAGE")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://image.cn-north-4.myhuaweicloud.com",
                        "https://image.cn-north-4.myhuaweicloud.cn")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://image.cn-north-1.myhuaweicloud.com",
                        "https://image.cn-north-1.myhuaweicloud.cn")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://image.ap-southeast-1.myhuaweicloud.com",
                        "https://image.ap-southeast-1.myhuaweicloud.cn")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://image.ap-southeast-3.myhuaweicloud.com",
                        "https://image.ap-southeast-3.myhuaweicloud.cn")
    CN_EAST_3 = Region("cn-east-3",
                        "https://image.cn-east-3.myhuaweicloud.com",
                        "https://image.cn-east-3.myhuaweicloud.cn")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-east-3": CN_EAST_3,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Image': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
