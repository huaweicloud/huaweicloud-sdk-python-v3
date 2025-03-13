# coding: utf-8

from __future__ import absolute_import

import importlib
import os
import threading
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from huaweicloudsdkkvs.v1.config.kvs_sdk_config import KvsSdkConfig
from huaweicloudsdkkvs.v1.managed_kvs_client import ManagedKvsClient
from huaweicloudsdkkvs.v1.model.credential import Credential
from huaweicloudsdkkvs.v1.util.thread_safe_utils import ThreadSafeDict, ThreadSafeList


class KvsSdkConfigManager:
    class __ConfigFileModifyHandler(FileSystemEventHandler):
        def __init__(self, config_manager, reload_interval):
            self.config_manager = config_manager
            self._reload_interval = reload_interval
            self._last_event_time = time.time()
            self._processing = False

        def on_modified(self, event):
            if not self._processing and not event.is_directory:
                self._processing = True
                threading.Timer(self._reload_interval, self._process_event).start()

        def _process_event(self):
            current_time = time.time()
            if current_time - self._last_event_time >= self._reload_interval:
                self.config_manager.reload_config()
                self.config_manager.load_aksk_config()
                self.config_manager.load_endpoint_config()
                self._last_event_time = current_time
            self._processing = False

    def __init__(self, config_file_path, is_async_client, kvs_client_map, old_kvs_client_maps, logger=None,
                 customized_http_config=None, http_handler=None, exception_handler=None):
        self._logger = logger
        self.model_package = importlib.import_module("huaweicloudsdkkvs.v1.model")
        self._config_file_path = config_file_path or os.path.join(os.path.dirname(__file__), '../../../kvs-sdk.config')
        self._is_async_client = is_async_client

        self._credential = Credential()
        self._endpoints = ThreadSafeList()
        self.kvs_client_map = kvs_client_map
        self.old_kvs_client_maps = old_kvs_client_maps

        self._kvs_sdk_config = KvsSdkConfig(self._config_file_path, self._is_async_client, self._logger)
        if customized_http_config is not None:
            self._kvs_sdk_config.customize_http_config = customized_http_config
        self._http_handler = http_handler
        self._exception_handler = exception_handler

        self.load_aksk_config()
        self.load_endpoint_config()
        self.observer = Observer()
        event_handler = self.__ConfigFileModifyHandler(self, self._kvs_sdk_config.reload_interval / 1000.0)
        self.observer.schedule(event_handler, path=os.path.dirname(self._config_file_path), recursive=False)
        self.observer.start()

    @property
    def kvs_sdk_config(self):
        """Gets the kvs sdk config.

         kvs sdk config.

        :return: The kvs sdk config.
        :rtype: class:`huaweicloudsdkkvs.v1.model.KvsSdkConfig`
        """
        return self._kvs_sdk_config

    def reload_config(self):
        self._kvs_sdk_config.load_config()

    def load_aksk_config(self):
        if self._credential.ak is None or self._credential.ak != self._kvs_sdk_config.ak \
                or self._credential.sk is None or self._credential.sk != self._kvs_sdk_config.sk:
            self._credential.ak = self._kvs_sdk_config.ak
            self._credential.sk = self._kvs_sdk_config.sk
            self._credential.sts_token = self._kvs_sdk_config.sts_token

            new_kvs_client_map = ThreadSafeDict()
            for key in self.kvs_client_map.keys():
                new_kvs_client_map.set(key, self.kvs_client_map.get(key))

            self._endpoints.clear()
            self.kvs_client_map.clear()
            if new_kvs_client_map.size() != 0:
                self.old_kvs_client_maps.set(time.time_ns(), new_kvs_client_map)

    def load_endpoint_config(self):
        new_endpoint_list = self._kvs_sdk_config.load_endpoint_list()
        filtered_endpoint_list = []
        for endpoint in new_endpoint_list:
            if not self.kvs_client_map.include_endpoint(endpoint):
                filtered_endpoint_list.append(endpoint)

        for endpoint in filtered_endpoint_list:
            new_kvs_client = ManagedKvsClient(endpoint, self._kvs_sdk_config, self._http_handler,
                                              self._exception_handler)
            self.kvs_client_map.set(self.kvs_client_map.size() + 1, new_kvs_client)

    def stop_observer(self):
        self.observer.stop()
