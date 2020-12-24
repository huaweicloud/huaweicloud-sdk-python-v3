# coding: utf-8

from huaweicloudsdkcore.region.region import Region


class CloudtestRegion:
    def __init__(self):
        pass

    CN_NORTH_1 = Region(id="cn-north-1", endpoint="https://cloudtest-ext.cn-north-1.myhuaweicloud.com/v1/projects")

    CN_NORTH_4 = Region(id="cn-north-4", endpoint="https://cloudtest-ext.cn-north-4.myhuaweicloud.com")

    CN_SOUTH_1 = Region(id="cn-south-1", endpoint="https://cloudtest-ext.cn-south-1.myhuaweicloud.com")

    CN_EAST_2 = Region(id="cn-east-2", endpoint="https://cloudtest-ext.cn-east-2.myhuaweicloud.cn")

    CN_EAST_3 = Region(id="cn-east-3", endpoint="https://cloudtest-ext.cn-east-3.myhuaweicloud.com")


