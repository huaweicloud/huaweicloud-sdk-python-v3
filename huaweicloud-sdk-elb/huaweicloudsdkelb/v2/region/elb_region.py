# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region


class ElbRegion:
    def __init__(self):
        pass

    AF_SOUTH_1 = Region(id="af-south-1", endpoint="https://elb.af-south-1.myhuaweicloud.com")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://elb.cn-north-4.myhuaweicloud.com")

    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://elb.cn-north-1.myhuaweicloud.com")

    CN_NORTH_2 = Region(id="cn-north-2", endpoint="https://elb.cn-north-2.myhuaweicloud.com")

    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://elb.cn-east-2.myhuaweicloud.com")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://elb.cn-east-3.myhuaweicloud.com")

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://elb.cn-south-1.myhuaweicloud.com")

    CN_SOUTH_2 = Region(id="cn-south-2", endpoint="https://elb.cn-south-2.myhuaweicloud.com")

    CN_SOUTHWEST_2 = Region(id="cn-southwest-2", endpoint="https://elb.cn-southwest-2.myhuaweicloud.com")

    AP_SOUTHEAST_2 = Region(id="ap-southeast-2", endpoint="https://elb.ap-southeast-2.myhuaweicloud.com")

    AP_SOUTHEAST_1 = Region(id="ap-southeast-1", endpoint="https://elb.ap-southeast-1.myhuaweicloud.com")

    AP_SOUTHEAST_3 = Region(id="ap-southeast-3", endpoint="https://elb.ap-southeast-3.myhuaweicloud.com")

    SA_ARGENTINA_1 = Region(id="sa-argentina-1", endpoint="https://elb.sa-argentina-1.myhuaweicloud.com")

    SA_PERU_1 = Region(id="sa-peru-1", endpoint="https://elb.sa-peru-1.myhuaweicloud.com")

    NA_MEXICO_1 = Region(id="na-mexico-1", endpoint="https://elb.na-mexico-1.myhuaweicloud.com")

    LA_SOUTH_2 = Region(id="la-south-2", endpoint="https://elb.la-south-2.myhuaweicloud.com")

    SA_CHILE_1 = Region(id="sa-chile-1", endpoint="https://elb.sa-chile-1.myhuaweicloud.com")

    SA_BRAZIL_1 = Region(id="sa-brazil-1", endpoint="https://elb.sa-brazil-1.myhuaweicloud.com")

    static_fields = {
        "af-south-1": AF_SOUTH_1,
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-north-2": CN_NORTH_2,
        "cn-east-2": CN_EAST_2,
        "cn-east-3": CN_EAST_3,
        "cn-south-1": CN_SOUTH_1,
        "cn-south-2": CN_SOUTH_2,
        "cn-southwest-2": CN_SOUTHWEST_2,
        "ap-southeast-2": AP_SOUTHEAST_2,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
        'sa-argentina-1': SA_ARGENTINA_1,
        'sa-peru-1': SA_PERU_1,
        'na-mexico-1': NA_MEXICO_1,
        'la-south-2': LA_SOUTH_2,
        'sa-chile-1': SA_CHILE_1,
        'sa-brazil-1': SA_BRAZIL_1,
    }

    @staticmethod
    def value_of(region_id, static_fields=types.MappingProxyType(static_fields) if six.PY3 else static_fields):
        if region_id is None or len(region_id) == 0:
            raise KeyError("Unexpected empty parameter: region_id.")
        if not static_fields.get(region_id):
            raise KeyError("Unexpected region_id: " + region_id)
        return static_fields.get(region_id)


