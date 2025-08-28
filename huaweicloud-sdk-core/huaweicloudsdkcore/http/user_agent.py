# coding: utf-8
"""
 Copyright 2025 Huawei Technologies Co.,Ltd.

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

import platform
import re
import os
import stat
import uuid
from huaweicloudsdkcore.utils.filepath_utils import get_home_path
from huaweicloudsdkcore.utils.string_utils import replace_invalid_character


class _UserAgent:
    _DEFAULT_APPLICATION_ID_FILE_NAME = "application_id"
    _DEFAULT_FILE_DIR = ".huaweicloud"
    _DEFAULT_VALUE = ""

    _UUID_PATTERN = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$')

    def __init__(self):
        self._os_name = self._get_platform_info(platform.system)
        self._os_version = self._get_platform_info(platform.version)
        self._os_arch = self._get_platform_info(platform.machine)

        self._python_version = self._get_platform_info(platform.python_version)
        self._python_implementation = self._get_platform_info(platform.python_implementation)

        self._app_file_path = self._get_app_file_path()
        self._app_id = self._get_app_id()

        self._user_agent = self._generate_user_agent_string()

    @property
    def user_agent(self):
        return self._user_agent

    def _get_platform_info(self, func):
        try:
            return func() or self._DEFAULT_VALUE
        except Exception:
            return self._DEFAULT_VALUE

    def _get_app_file_path(self):
        home_path = get_home_path()
        return os.path.join(home_path, self._DEFAULT_FILE_DIR, self._DEFAULT_APPLICATION_ID_FILE_NAME
                            ) if home_path else home_path

    def _read_app_id(self):
        try:
            if not os.path.isfile(self._app_file_path):
                return None

            with open(self._app_file_path, "r", encoding="utf-8") as file:
                app_id = file.readline().strip()
                return app_id if app_id else None
        except Exception:
            return None

    def _store_app_id(self, app_id):
        try:
            os.makedirs(os.path.dirname(self._app_file_path), mode=0o750, exist_ok=True)
            with os.fdopen(
                    os.open(self._app_file_path,
                            os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
                            stat.S_IWUSR | stat.S_IRUSR | stat.S_IRGRP),
                    'w',
                    encoding="utf-8") as file:
                file.write(app_id)
            return True
        except Exception:
            return False

    def _get_app_id(self):
        if not self._app_file_path:
            return self._DEFAULT_VALUE

        app_id = self._read_app_id()
        if app_id and self._UUID_PATTERN.match(app_id):
            return app_id

        new_app_id = str(uuid.uuid4())
        if self._store_app_id(new_app_id):
            return new_app_id
        return self._DEFAULT_VALUE

    def _build_os_metadata(self):
        if self._os_name:
            return [f"os/{'#'.join([self._os_name, self._os_version, self._os_arch])}"]
        return []

    def _build_python_metadata(self):
        py_meta = [
            f"python/{self._python_version}"
        ]
        if self._python_implementation:
            py_meta.append(f"impl/{self._python_implementation}")
        return py_meta

    def _generate_user_agent_string(self):
        environment_meta = ' '.join(replace_invalid_character(metadata) for metadata in [
            *self._build_os_metadata(),
            *self._build_python_metadata()
        ])
        if not self._app_id:
            return environment_meta

        return '; '.join([environment_meta, f"app/{self._app_id}"])

user_agent_string = _UserAgent().user_agent
