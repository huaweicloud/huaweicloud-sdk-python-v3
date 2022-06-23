# coding: utf-8
"""
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache LICENSE, Version 2.0 (the
 "LICENSE"); you may not use this file except in compliance
 with the LICENSE.  You may obtain a copy of the LICENSE at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the LICENSE is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the LICENSE for the
 specific language governing permissions and limitations
 under the LICENSE.
"""

import os
from abc import abstractmethod

from huaweicloudsdkcore.region.cache import ProfileRegionCache, EnvRegionCache
from huaweicloudsdkcore.region.region import Region

from huaweicloudsdkcore.utils import six_utils


class RegionProvider(six_utils.get_abstract_meta_class()):

    def __init__(self, service_name):
        self._service_name = service_name.upper()

    @abstractmethod
    def get_region(self, region_id):
        pass


class RegionProviderChain(RegionProvider):

    def __init__(self, service_name, providers):
        super(RegionProviderChain, self).__init__(service_name)
        self._providers = providers

    def get_region(self, region_id):
        for provider in self._providers:
            region = provider.get_region(region_id)
            if region:
                return region
        return None

    @staticmethod
    def get_default_region_provider_chain(service_name):
        providers = [EnvRegionProvider(service_name), ProfileRegionProvider(service_name)]
        return RegionProviderChain(service_name, providers)


class EnvRegionProvider(RegionProvider):
    _REGION_ENV_PREFIX = "HUAWEICLOUD_SDK_REGION"

    def get_region(self, region_id):

        cache = EnvRegionCache()
        region = cache.get(self._service_name)
        if region:
            return region

        env_name = "{}_{}_{}".format(self._REGION_ENV_PREFIX, self._service_name, region_id.replace("-", "_").upper())
        endpoint = os.getenv(env_name)
        if not endpoint:
            return None

        region = Region(region_id, endpoint)
        cache.set(self._service_name + region_id, region)
        return region


class ProfileRegionProvider(RegionProvider):
    def get_region(self, region_id):
        return ProfileRegionCache().get(self._service_name + region_id)
