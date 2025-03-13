# coding: utf-8

from __future__ import absolute_import

import queue
import time
from concurrent.futures import ThreadPoolExecutor

from huaweicloudsdkcore.exceptions.exceptions import ConnectionException, RequestTimeoutException

from huaweicloudsdkkvs.v1 import CheckHealthRequestBody, CheckHealthRequest


class KvsClientHeartbeatKeeper:
    def __init__(self, kvs_client_map, heartbeat_check_interval_ms, heartbeat_check_threadpool_size, logger):
        self._logger = logger
        self._kvs_client_map = kvs_client_map
        self._heartbeat_check_interval = heartbeat_check_interval_ms / 1000.0
        self.health_check_thread_pool = BoundThreadPoolExecutor(max_workers=heartbeat_check_threadpool_size,
                                                                queue_size=heartbeat_check_threadpool_size * 100,
                                                                thread_name_prefix="kvs_client_heartbeat_thread_")
        self.thread_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="kvs_client_heartbeat_keeper_thread_")
        self.thread_pool.submit(self._heartbeat_keeper_task)

    def close(self):
        self.health_check_thread_pool.shutdown()
        self.thread_pool.shutdown()

    def _heartbeat_keeper_task(self):
        for index in self._kvs_client_map.keys():
            try:
                self.health_check_thread_pool.submit(self._health_check_task, self._kvs_client_map.get(index))
            except queue.Full:
                self._logger.info("heartbeat keeper threadpool is full, %s healthcheck has been skipped!",
                                  self._kvs_client_map.get(index).endpoint.name)
            time.sleep(self._heartbeat_check_interval)
            self.thread_pool.submit(self._heartbeat_keeper_task)

    def _health_check_task(self, kvs_client):
        is_usable = True
        request = CheckHealthRequest(CheckHealthRequestBody(1))
        try:
            if kvs_client.is_async_client:
                kvs_client.client.check_health_async(request)
            else:
                kvs_client.client.check_health(request)
        except (ConnectionException, RequestTimeoutException) as e:
            is_usable = False
            self._logger.warn("Network channel throw Exception, set %s client to unusable, errorInfo: %s",
                              kvs_client.endpoint.name, e)
        except Exception as e:
            self._logger.debug("get healthCheckResponse from future of AsyncClient failed!, errorInfo: %s", e)
        kvs_client.is_usable = is_usable


class BoundThreadPoolExecutor(ThreadPoolExecutor):
    def __init__(self, max_workers=None, queue_size=None, thread_name_prefix=''):
        super().__init__(max_workers, thread_name_prefix)
        self._queue_size = queue_size
        self._work_queue = queue.SimpleQueue()

    def submit(self, fn, *args, **kwargs):
        if self._work_queue.qsize() >= self._queue_size:
            raise queue.Full("Task queue is full")
        return super().submit(fn, *args, **kwargs)
