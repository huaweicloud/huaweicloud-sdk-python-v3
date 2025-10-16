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
from unittest.mock import patch, MagicMock, mock_open

import pytest


@pytest.fixture
def mock_platform(monkeypatch):
    monkeypatch.setattr(platform, 'system', MagicMock(return_value="Linux"))
    monkeypatch.setattr(platform, 'version', MagicMock(return_value="5.10.0"))
    monkeypatch.setattr(platform, 'machine', MagicMock(return_value="x86_64"))
    monkeypatch.setattr(platform, 'python_version', MagicMock(return_value="3.6.8"))
    monkeypatch.setattr(platform, 'python_implementation', MagicMock(return_value="CPython"))


@pytest.fixture
def mock_file_utils(monkeypatch):
    monkeypatch.setattr(
        "huaweicloudsdkcore.utils.filepath_utils.get_home_path",
        MagicMock(return_value='/opt')
    )
    return '/opt'


def test_platform_info_safety(mock_platform):
    assert platform.system() == "Linux"
    assert platform.version() == "5.10.0"
    assert platform.machine() == "x86_64"
    assert platform.python_version() == "3.6.8"
    assert platform.python_implementation() == "CPython"


def test_app_id_read_existing(mock_platform, mock_file_utils):
    existing_id = "123e4567-e89b-12d3-a456-426614174000"
    with patch("builtins.open", mock_open(read_data=existing_id)), \
         patch("os.path.exists", MagicMock(return_value=True)), \
         patch("os.path.isfile", MagicMock(return_value=True))   :
        from huaweicloudsdkcore.http.user_agent import _UserAgent
        agent = _UserAgent()
        assert agent._app_id == existing_id
        assert agent.user_agent == "os/Linux#5.10.0#x86_64 python/3.6.8 impl/CPython; app/123e4567-e89b-12d3-a456-426614174000"


def test_app_id_file_not_existing(mock_platform, mock_file_utils):
    """测试文件操作错误处理"""
    # 模拟读取错误
    with patch("os.open", mock_open()), \
         patch("os.path.exists", MagicMock(return_value=False)), \
         patch("os.makedirs", MagicMock(return_value=True)):
        from huaweicloudsdkcore.http.user_agent import _UserAgent
        agent = _UserAgent()
        assert agent._app_id is not None


def test_write_app_id_file_error(mock_platform, mock_file_utils):
    with patch("os.open", side_effect=OSError("Read error")), \
         patch("os.path.isfile", MagicMock(return_value=False)), \
         patch("os.makedirs", MagicMock(return_value=True)):
        from huaweicloudsdkcore.http.user_agent import _UserAgent
        agent = _UserAgent()
        print(agent.user_agent)
        assert not agent._app_id
        assert agent.user_agent == "os/Linux#5.10.0#x86_64 python/3.6.8 impl/CPython"

if __name__ == '__main__':
    pytest.main()

