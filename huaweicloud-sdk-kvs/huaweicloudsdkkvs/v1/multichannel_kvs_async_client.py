# coding: utf-8

from __future__ import absolute_import

import logging
import time
from concurrent.futures import ThreadPoolExecutor

from huaweicloudsdkcore.exceptions.exceptions import RequestTimeoutException, ConnectionException, SdkException

from huaweicloudsdkkvs.v1.abstract_multichannel_kvs_client import AbstractMultichannelKvsClient
from huaweicloudsdkkvs.v1.config.kvs_sdk_config_manager import KvsSdkConfigManager
from huaweicloudsdkkvs.v1.kvs_client_heartbeat_keeper import KvsClientHeartbeatKeeper
from huaweicloudsdkkvs.v1.kvs_async_client_interface import KvsAsyncClientInterface


class MultichannelKvsAsyncClient(AbstractMultichannelKvsClient, KvsAsyncClientInterface):
    def __init__(self, config_file_path, customized_http_config=None, http_handler=None, exception_handler=None):
        super(MultichannelKvsAsyncClient, self).__init__()
        self._logger = self._init_logger()
        self._config_manager = KvsSdkConfigManager(config_file_path, True, self._kvs_client_map,
                                                         self._old_kvs_client_maps, self._logger, customized_http_config,
                                                         http_handler, exception_handler)
        self._config = self._config_manager.kvs_sdk_config
        self._total_timeout = self._config.connection_timeout + self._config.read_timeout
        self._heartbeat_keeper = KvsClientHeartbeatKeeper(self._kvs_client_map, self._config.heartbeat_interval,
                                                                self._config.heartbeat_thread_pool_size, self._logger)
        self.thread_pool = ThreadPoolExecutor(max_workers=1, thread_name_prefix="kvs_client_clean_old_maps_thread_")
        self.thread_pool.submit(self._old_client_map_clean_task)

    @classmethod
    def _init_logger(cls):
        logger_name = 'KVS-multichannel-SDK-%s' % cls.__name__
        logger = logging.getLogger(logger_name)
        logger.propagate = False
        return logger

    def close(self):
        self._heartbeat_keeper.close()
        self.thread_pool.shutdown()

    @property
    def config(self):
        """Gets the multichannel sdk config.

        :return: The multichannel sdk config.
        :rtype: class:`huaweicloudsdkkvs.v1.model.KvsSdkConfig`
        """
        return self._config

    @property
    def old_kvs_client_maps(self):
        """Gets the old kvs client maps

        :return: The old kvs client maps
        :rtype: Dict{int, class:`huaweicloudsdkkvs.v1.model.KvsSdkConfig`}
        """
        return self._old_kvs_client_maps

    def _old_client_map_clean_task(self):
        removed_maps = []
        for clean_time in self._old_kvs_client_maps.keys():
            if time.time_ns() > clean_time + self._total_timeout * 1000000:
                removed_maps.append(clean_time)
        for clean_time in removed_maps:
            self._old_kvs_client_maps.delete(clean_time)
        time.sleep(self._total_timeout / 1000.0)
        self.thread_pool.submit(self._old_client_map_clean_task)


    def create_table_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.create_table_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s CreateTable throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry CreateTable " + str(retry_count) + " times, and failed!")

    def create_table_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.create_table_invoker(request)


    def delete_table_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.delete_table_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s DeleteTable throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry DeleteTable " + str(retry_count) + " times, and failed!")

    def delete_table_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.delete_table_invoker(request)


    def describe_table_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.describe_table_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s DescribeTable throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry DescribeTable " + str(retry_count) + " times, and failed!")

    def describe_table_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.describe_table_invoker(request)


    def list_store_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.list_store_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s ListStore throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry ListStore " + str(retry_count) + " times, and failed!")

    def list_store_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.list_store_invoker(request)


    def list_table_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.list_table_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s ListTable throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry ListTable " + str(retry_count) + " times, and failed!")

    def list_table_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.list_table_invoker(request)


    def batch_get_kv_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.batch_get_kv_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s BatchGetKv throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry BatchGetKv " + str(retry_count) + " times, and failed!")

    def batch_get_kv_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.batch_get_kv_invoker(request)


    def batch_write_kv_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.batch_write_kv_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s BatchWriteKv throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry BatchWriteKv " + str(retry_count) + " times, and failed!")

    def batch_write_kv_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.batch_write_kv_invoker(request)


    def delete_kv_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.delete_kv_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s DeleteKv throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry DeleteKv " + str(retry_count) + " times, and failed!")

    def delete_kv_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.delete_kv_invoker(request)


    def get_kv_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.get_kv_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s GetKv throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry GetKv " + str(retry_count) + " times, and failed!")

    def get_kv_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.get_kv_invoker(request)


    def put_kv_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.put_kv_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s PutKv throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry PutKv " + str(retry_count) + " times, and failed!")

    def put_kv_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.put_kv_invoker(request)


    def scan_kv_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.scan_kv_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s ScanKv throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry ScanKv " + str(retry_count) + " times, and failed!")

    def scan_kv_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.scan_kv_invoker(request)


    def scan_skey_kv_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.scan_skey_kv_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s ScanSkeyKv throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry ScanSkeyKv " + str(retry_count) + " times, and failed!")

    def scan_skey_kv_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.scan_skey_kv_invoker(request)


    def update_kv_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.update_kv_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s UpdateKv throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry UpdateKv " + str(retry_count) + " times, and failed!")

    def update_kv_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.update_kv_invoker(request)


    def check_health_async(self, request):
        retry_count = 0
        while retry_count < self._config.api_retry_count:
            managed_client = self.get_kvs_client_by_polling_with_retry(retry_count)
            try:
                return managed_client.client.check_health_async(request)
            except (ConnectionException, RequestTimeoutException) as e:
                managed_client.is_usable = False
                retry_count += 1
                self._logger.info("this is client: %s CheckHealth throwing Exception %d time. errorInfo: %s",
                                  managed_client.endpoint.name, retry_count, e)
        raise SdkException("retry CheckHealth " + str(retry_count) + " times, and failed!")

    def check_health_async_invoker(self, request):
        return self.get_kvs_client_by_polling().client.check_health_invoker(request)

