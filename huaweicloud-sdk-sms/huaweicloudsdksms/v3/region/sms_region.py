# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region


class SmsRegion:
    def __init__(self):
        pass

    AP_SOUTHEAST_1 = Region(id="ap-southeast-1", endpoint="https://sms.ap-southeast-1.myhuaweicloud.com")

    static_fields = {
        "ap-southeast-1": AP_SOUTHEAST_1,
    }

    @staticmethod
    def value_of(region_id, static_fields=types.MappingProxyType(static_fields) if six.PY3 else static_fields):
        if region_id is None or len(region_id) == 0:
            raise KeyError("Unexpected empty parameter: region_id.")
        if not static_fields.get(region_id):
            raise KeyError("Unexpected region_id: " + region_id)
        return static_fields.get(region_id)


