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
from threading import Lock

import six


class SingletonMeta(type):
    _instances = {}

    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances.get(cls)


def get_abstract_meta_class():
    if six.PY3:
        from abc import ABC
        return ABC

    from abc import ABCMeta
    return six.with_metaclass(ABCMeta)


def get_singleton_meta_class():
    return six.with_metaclass(SingletonMeta)
