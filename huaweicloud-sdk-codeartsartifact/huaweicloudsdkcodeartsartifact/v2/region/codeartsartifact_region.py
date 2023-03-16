# coding: utf-8

import types
import six

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CodeArtsArtifactRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CODEARTSARTIFACT")

    CN_EAST_3 = Region("cn-east-3",
                        "https://cloudartifacts-ext.cn-east-3.myhuaweicloud.com")

    static_fields = {
        "cn-east-3": CN_EAST_3,
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

