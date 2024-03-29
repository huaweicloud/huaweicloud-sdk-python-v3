# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class IdentityCenterStoreRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("IDENTITYCENTERSTORE")

    CN_EAST_3 = Region("cn-east-3",
                        "https://identitystore.cn-east-3.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://identitystore.cn-north-4.myhuaweicloud.com")
    AP_SOUTHEAST_4 = Region("ap-southeast-4",
                        "https://identitystore.ap-southeast-4.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://identitystore.ap-southeast-3.myhuaweicloud.com")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://identitystore.ap-southeast-2.myhuaweicloud.com")

    static_fields = {
        "cn-east-3": CN_EAST_3,
        "cn-north-4": CN_NORTH_4,
        "ap-southeast-4": AP_SOUTHEAST_4,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "ap-southeast-2": AP_SOUTHEAST_2,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'IdentityCenterStore': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
