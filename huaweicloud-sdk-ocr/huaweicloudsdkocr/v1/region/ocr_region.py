# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class OcrRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("OCR")

    CN_NORTH_4 = Region("cn-north-4",
                        "https://ocr.cn-north-4.myhuaweicloud.com",
                        "https://ocr.cn-north-4.myhuaweicloud.cn")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://ocr.cn-south-1.myhuaweicloud.com",
                        "https://ocr.cn-south-1.myhuaweicloud.cn")
    CN_EAST_3 = Region("cn-east-3",
                        "https://ocr.cn-east-3.myhuaweicloud.com",
                        "https://ocr.cn-east-3.myhuaweicloud.cn")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://ocr.cn-north-1.myhuaweicloud.com",
                        "https://ocr.cn-north-1.myhuaweicloud.cn")
    AP_SOUTHEAST_2 = Region("ap-southeast-2",
                        "https://ocr.ap-southeast-2.myhuaweicloud.com",
                        "https://ocr.ap-southeast-2.myhuaweicloud.cn")
    CN_SOUTHWEST_2 = Region("cn-southwest-2",
                        "https://ocr.cn-southwest-2.myhuaweicloud.com",
                        "https://ocr.cn-southwest-2.myhuaweicloud.cn")
    AP_SOUTHEAST_1 = Region("ap-southeast-1",
                        "https://ocr.ap-southeast-1.myhuaweicloud.com",
                        "https://ocr.ap-southeast-1.myhuaweicloud.cn")
    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://ocr.ap-southeast-3.myhuaweicloud.com",
                        "https://ocr.ap-southeast-3.myhuaweicloud.cn")
    LA_SOUTH_2 = Region("la-south-2",
                        "https://ocr.la-south-2.myhuaweicloud.com",
                        "https://ocr.la-south-2.myhuaweicloud.cn")
    AF_SOUTH_1 = Region("af-south-1",
                        "https://ocr.af-south-1.myhuaweicloud.com",
                        "https://ocr.af-south-1.myhuaweicloud.cn")
    LA_NORTH_2 = Region("la-north-2",
                        "https://ocr.la-north-2.myhuaweicloud.com")

    static_fields = {
        "cn-north-4": CN_NORTH_4,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-north-1": CN_NORTH_1,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        "la-south-2": LA_SOUTH_2,
        "af-south-1": AF_SOUTH_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'Ocr': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
