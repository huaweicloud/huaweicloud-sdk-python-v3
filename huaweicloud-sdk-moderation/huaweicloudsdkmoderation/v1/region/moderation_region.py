# coding: utf-8

import types

from huaweicloudsdkcore.region.region import Region


class ModerationRegion:
    def __init__(self):
        pass

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://moderation.cn-north-4.myhuaweicloud.com")

    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://moderation.cn-north-1.myhuaweicloud.com")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://moderation.cn-east-3.myhuaweicloud.com")

    AP_SOUTHEAST_1 = Region(id="ap-southeast-1", endpoint="https://moderation.ap-southeast-1.myhuaweicloud.com")

    AP_SOUTHEAST_3 = Region(id="ap-southeast-3", endpoint="https://moderation.ap-southeast-3.myhuaweicloud.com")

    static_fields = types.MappingProxyType({
        "cn-north-4": CN_NORTH_4,
        "cn-north-1": CN_NORTH_1,
        "cn-east-3": CN_EAST_3,
        "ap-southeast-1": AP_SOUTHEAST_1,
        "ap-southeast-3": AP_SOUTHEAST_3,
    })

    @staticmethod
    def value_of(region_id, static_fields=static_fields):
        if region_id is None or len(region_id) == 0:
            raise KeyError("Unexpected empty parameter: region_id.")
        if not static_fields.get(region_id):
            raise KeyError("Unexpected region_id: " + region_id)
        return static_fields.get(region_id)


