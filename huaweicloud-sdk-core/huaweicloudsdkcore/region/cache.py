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
import yaml

from huaweicloudsdkcore.region.region import Region
from huaweicloudsdkcore.utils import six_utils, filepath_utils


class EnvRegionCache(six_utils.get_singleton_meta_class()):
    def __init__(self):
        self._value = {}

    def set(self, name, region):
        self._value[name] = region

    def get(self, name):
        return self._value.get(name)


class ProfileRegionCache(six_utils.get_singleton_meta_class()):
    _REGIONS_FILE_ENV_NAME = "HUAWEICLOUD_SDK_REGIONS_FILE"
    _DEFAULT_REGIONS_FILE_DIR = ".huaweicloud"
    _DEFAULT_REGIONS_FILE = "regions.yaml"

    def __init__(self):
        self._value = self._resolve_profile()

    def get(self, name):
        return self._value.get(name)

    @classmethod
    def _resolve_profile(cls):
        result = {}

        path = cls._get_regions_file_path()
        if not filepath_utils.is_path_exist(path):
            return result

        with open(path, "r") as f:
            _dict = yaml.safe_load(f)

        for service, regions in _dict.items():
            for region in regions:
                _id = region.get("id")
                if not _id:
                    continue

                endpoints = region.get("endpoints")
                if not endpoints:
                    endpoints = []
                endpoint = region.get("endpoint")
                if endpoint:
                    endpoints.append(endpoint)

                if endpoints:
                    result[service.upper() + _id] = Region(_id, *endpoints)

        return result

    @classmethod
    def _get_regions_file_path(cls):
        regions_file = os.environ.get(cls._REGIONS_FILE_ENV_NAME)
        if regions_file:
            return regions_file

        home_path = filepath_utils.get_home_path()
        return os.path.join(home_path,
                            cls._DEFAULT_REGIONS_FILE_DIR, cls._DEFAULT_REGIONS_FILE) if home_path else home_path
