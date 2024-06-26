# coding: utf-8
"""
 Copyright 2022 Huawei Technologies Co.,Ltd.

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
from sys import platform


def get_home_path():
    home_path = None
    if platform.startswith("win32"):
        home_path = os.environ.get("USERPROFILE")
    elif platform.startswith("linux") or platform.startswith("darwin"):
        home_path = os.environ.get("HOME")

    return home_path


def is_path_exist(path):
    if not path:
        return False
    return os.path.exists(path)


def ensure_file_in_rb_mode(_file):
    if isinstance(_file, str):
        if not os.path.isfile(_file):
            raise ValueError("invalid file path: " + _file)
        return open(_file, "rb")

    if not hasattr(_file, "read") or not hasattr(_file, "mode"):
        raise TypeError("invalid file type")

    if _file.mode != "rb":
        _file.close()
        raise ValueError("invalid file mode, please open the file in 'rb' mode")
    return _file
