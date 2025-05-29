# coding: utf-8

from abc import ABC, abstractmethod


class KvsAsyncClientInterface(ABC):

    @abstractmethod
    def create_table_async(self, request):
        pass

    @abstractmethod
    def create_table_async_invoker(self, request):
        pass

    @abstractmethod
    def delete_table_async(self, request):
        pass

    @abstractmethod
    def delete_table_async_invoker(self, request):
        pass

    @abstractmethod
    def describe_table_async(self, request):
        pass

    @abstractmethod
    def describe_table_async_invoker(self, request):
        pass

    @abstractmethod
    def list_store_async(self, request):
        pass

    @abstractmethod
    def list_store_async_invoker(self, request):
        pass

    @abstractmethod
    def list_table_async(self, request):
        pass

    @abstractmethod
    def list_table_async_invoker(self, request):
        pass

    @abstractmethod
    def batch_get_kv_async(self, request):
        pass

    @abstractmethod
    def batch_get_kv_async_invoker(self, request):
        pass

    @abstractmethod
    def batch_write_kv_async(self, request):
        pass

    @abstractmethod
    def batch_write_kv_async_invoker(self, request):
        pass

    @abstractmethod
    def delete_kv_async(self, request):
        pass

    @abstractmethod
    def delete_kv_async_invoker(self, request):
        pass

    @abstractmethod
    def get_kv_async(self, request):
        pass

    @abstractmethod
    def get_kv_async_invoker(self, request):
        pass

    @abstractmethod
    def put_kv_async(self, request):
        pass

    @abstractmethod
    def put_kv_async_invoker(self, request):
        pass

    @abstractmethod
    def scan_kv_async(self, request):
        pass

    @abstractmethod
    def scan_kv_async_invoker(self, request):
        pass

    @abstractmethod
    def scan_skey_kv_async(self, request):
        pass

    @abstractmethod
    def scan_skey_kv_async_invoker(self, request):
        pass

    @abstractmethod
    def update_kv_async(self, request):
        pass

    @abstractmethod
    def update_kv_async_invoker(self, request):
        pass

    @abstractmethod
    def check_health_async(self, request):
        pass

    @abstractmethod
    def check_health_async_invoker(self, request):
        pass
