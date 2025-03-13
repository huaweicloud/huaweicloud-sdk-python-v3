# coding: utf-8
import random
import threading
import time
from abc import ABC

from huaweicloudsdkcore.exceptions.exceptions import SdkException

from huaweicloudsdkkvs.v1.util.thread_safe_utils import ThreadSafeDict, AtomicInteger

BASE_OF_EXPONENT = 2


class AbstractMultichannelKvsClient(ABC):
    def __init__(self):
        self._lock = threading.Lock()
        self._kvs_client_map = ThreadSafeDict()
        self._old_kvs_client_maps = ThreadSafeDict()
        self._token_num = AtomicInteger(1)
        self._weight_count = AtomicInteger(0)

    def get_kvs_client_by_polling(self):
        select_count = 0
        kvs_client_num = 0
        with self._lock:
            while True:
                if select_count > self._kvs_client_map.size():
                    raise SdkException("all web channel of kvs clients are unusable! please wait and retry")
                select_count += 1
                kvs_client = self._kvs_client_map.get(self._token_num.get())
                if kvs_client.is_usable and self._weight_count.get() < kvs_client.endpoint.weight:
                    self._weight_count.increment()
                elif self._token_num.get() >= self._kvs_client_map.size():
                    self._token_num.set(1)
                    self._weight_count.set(1)
                else:
                    self._token_num.increment()
                    self._weight_count.set(1)
                if self._kvs_client_map.get(self._token_num.get()).is_usable:
                    break
            kvs_client_num = self._token_num.get()
        return self._kvs_client_map.get(kvs_client_num)

    def get_kvs_client_by_polling_with_retry(self, retry_count):
        if retry_count > 0:
            time.sleep(random.uniform(0, BASE_OF_EXPONENT ** retry_count))
        return self.get_kvs_client_by_polling()
