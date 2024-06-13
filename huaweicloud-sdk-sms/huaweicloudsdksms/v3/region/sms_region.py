# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class SmsRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("SMS")

    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://sms.ap-southeast-1.myhuaweicloud.com")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://sms.ap-southeast-3.myhuaweicloud.com")
    MY_KUALALUMPUR_1 = Region("my-kualalumpur-1",
                        "https://sms.my-kualalumpur-1.myhuaweicloud.com")
    RU_MOSCOW_1 = Region("ru-moscow-1",
                        "https://sms-api.ru-moscow-1.myhuaweicloud.com")

    static_fields = {
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "my-kualalumpur-1": MY_KUALALUMPUR_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Sms': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
