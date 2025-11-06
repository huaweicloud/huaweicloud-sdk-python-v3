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
from threading import Lock
from typing import Union


class SingletonMeta(type):
    _instances = {}

    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances.get(cls)


def ensure_binary(s: Union[str, bytes], encoding: str = "utf-8", errors: str = "strict") -> bytes:
    if isinstance(s, bytes):
        return s
    if isinstance(s, str):
        return s.encode(encoding, errors)

    raise TypeError(f"not expecting type '{type(s)}'")


def ensure_str(s: Union[str, bytes], encoding: str = "utf-8", errors: str = "strict") -> str:
    if isinstance(s, str):
        return s
    if isinstance(s, bytes):
        return s.decode(encoding, errors)

    raise TypeError(f"not expecting type '{type(s)}'")
