# coding: utf-8
"""
 Copyright 2024 Huawei Technologies Co.,Ltd.

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
from abc import abstractmethod
from random import randint

from huaweicloudsdkcore.utils import six_utils

_BASE_DELAY_MS = 10  # 10ms
_MAX_DELAY_MS = 60 * 1000  # 60s


class BackoffStrategy(six_utils.get_abstract_meta_class()):
    @abstractmethod
    def calculate_retry_delay_millis(self, retries):
        # type: (int) -> int
        pass


class NoBackoffStrategy(BackoffStrategy):
    def calculate_retry_delay_millis(self, retries):
        return 0


class ExponentialBackoffStrategy(BackoffStrategy):
    def calculate_retry_delay_millis(self, retries):
        return min(_MAX_DELAY_MS, _BASE_DELAY_MS * (2 ** retries))


class EqualJitterBackoffStrategy(ExponentialBackoffStrategy):
    def calculate_retry_delay_millis(self, retries):
        half_expo_delay = super(EqualJitterBackoffStrategy, self).calculate_retry_delay_millis(retries) // 2
        return half_expo_delay + randint(1, half_expo_delay)


class RandomJitterBackoffStrategy(ExponentialBackoffStrategy):
    def calculate_retry_delay_millis(self, retries):
        expo_delay = super(RandomJitterBackoffStrategy, self).calculate_retry_delay_millis(retries)
        return randint(1, expo_delay)


class DecorRelatedJitterBackoffStrategy(BackoffStrategy):
    def calculate_retry_delay_millis(self, retries):
        return min(_MAX_DELAY_MS, randint(_BASE_DELAY_MS, _BASE_DELAY_MS * 3))


class BackoffStrategies(object):
    NONE = NoBackoffStrategy()
    RANDOM_JITTER = RandomJitterBackoffStrategy()
    EQUAL_JITTER = EqualJitterBackoffStrategy()
    DECOR_RELATED_JITTER = DecorRelatedJitterBackoffStrategy()
