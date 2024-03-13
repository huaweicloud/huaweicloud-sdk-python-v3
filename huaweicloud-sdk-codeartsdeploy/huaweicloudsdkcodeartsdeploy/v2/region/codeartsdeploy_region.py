# coding: utf-8

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.region.provider import RegionProviderChain

class CodeArtsDeployRegion:
    _PROVIDER = RegionProviderChain.get_default_region_provider_chain("CODEARTSDEPLOY")

    AP_SOUTHEAST_3 = Region("ap-southeast-3",
                        "https://codearts-deploy.ap-southeast-3.myhuaweicloud.com")
    CN_SOUTH_1 = Region("cn-south-1",
                        "https://codearts-deploy.cn-south-1.myhuaweicloud.com")
    CN_EAST_3 = Region("cn-east-3",
                        "https://codearts-deploy.cn-east-3.myhuaweicloud.com")
    CN_EAST_2 = Region("cn-east-2",
                        "https://codearts-deploy.cn-east-2.myhuaweicloud.com")
    CN_NORTH_1 = Region("cn-north-1",
                        "https://codearts-deploy.cn-north-1.myhuaweicloud.com")
    CN_NORTH_4 = Region("cn-north-4",
                        "https://codearts-deploy.cn-north-4.myhuaweicloud.com")
    SA_BRAZIL_1 = Region("sa-brazil-1",
                        "https://codearts-deploy.sa-brazil-1.myhuaweicloud.com")
    LA_NORTH_2 = Region("la-north-2",
                        "https://codearts-deploy.la-north-2.myhuaweicloud.com")
    TR_WEST_1 = Region("tr-west-1",
                        "https://codearts-deploy.tr-west-1.myhuaweicloud.com")

    static_fields = {
        "ap-southeast-3": AP_SOUTHEAST_3,
        "cn-south-1": CN_SOUTH_1,
        "cn-east-3": CN_EAST_3,
        "cn-east-2": CN_EAST_2,
        "cn-north-1": CN_NORTH_1,
        "cn-north-4": CN_NORTH_4,
        "sa-brazil-1": SA_BRAZIL_1,
        "la-north-2": LA_NORTH_2,
        "tr-west-1": TR_WEST_1,
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

        raise KeyError("region_id '%s' is not in the following supported regions of service 'CodeArtsDeploy': [%s]" % (
            region_id, ", ".join(sorted(fields.keys()))))
