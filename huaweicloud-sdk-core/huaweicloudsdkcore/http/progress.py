# coding: utf-8
"""
 Copyright 2023 Huawei Technologies Co.,Ltd.
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

import threading
import time

import six
from urllib3.response import HTTPResponse

if six.PY3:
    from queue import Queue
else:
    from Queue import Queue

_CHUNK_SIZE = 65536
_INTERVAL = 102400


class ProgressNotifier(object):

    def __init__(self, callback=None, total_amount=-1, interval=_INTERVAL):
        self.callback = callback
        if self.callback is None or not callable(self.callback):
            raise TypeError('Invalid callback')
        self._total_amount = total_amount
        self._interval = interval
        self._transferred_amount = 0
        self._newly_transferred_amount = 0
        self._queue = Queue()
        self._start_checkpoint = None

    def _run(self):
        while True:
            data = self._queue.get()
            if data is None:
                self.callback(*self._calculate())
                self.callback = None
                self._queue = None
                break

            self._transferred_amount += data
            self._newly_transferred_amount += data
            if self._newly_transferred_amount >= self._interval and (
                    self._transferred_amount < self._total_amount or self._total_amount <= 0):
                self._newly_transferred_amount = 0
                self.callback(*self._calculate())

    def start(self):
        now = time.time()
        self._start_checkpoint = now
        t = threading.Thread(target=self._run)
        t.daemon = True
        t.start()

    def _calculate(self):
        total_seconds = time.time() - self._start_checkpoint
        return self._transferred_amount, self._total_amount, total_seconds if total_seconds > 0 else 0.001

    def send(self, data):
        if isinstance(data, six.integer_types):
            self._queue.put(data)

    def end(self):
        self._queue.put(None)


class ProgressRequestBody(object):
    def __init__(self, _file, notifier):
        self._file = _file
        self._notifier = notifier

    def __iter__(self):
        self._notifier.start()
        with self._file as f:
            while True:
                chunk = f.read(_CHUNK_SIZE)
                if not chunk:
                    self._notifier.end()
                    break
                self._notifier.send(len(chunk))
                yield chunk


class ProgressHTTPResponse(HTTPResponse):
    def __init__(self, notifier, *args, **kwargs):
        super(ProgressHTTPResponse, self).__init__(*args, **kwargs)
        self._notifier = notifier

    def read(self, amt=_CHUNK_SIZE, decode_content=None, cache_content=False):
        chunk = super(ProgressHTTPResponse, self).read(amt, decode_content, cache_content)
        if chunk:
            self._notifier.send(len(chunk))
        else:
            self._notifier.end()
        return chunk

    @classmethod
    def convert(cls, http_response, notifier):
        # type: (HTTPResponse, ProgressNotifier) -> None
        if not isinstance(http_response, cls.__base__):
            raise TypeError("can not convert non-HTTPResponse to ProgressHTTPResponse")
        http_response.__class__ = cls
        setattr(http_response, "_notifier", notifier)
        notifier.start()
