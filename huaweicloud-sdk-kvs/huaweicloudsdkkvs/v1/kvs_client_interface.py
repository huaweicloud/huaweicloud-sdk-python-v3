# coding: utf-8

from abc import ABC, abstractmethod


class KvsClientInterface(ABC):

    @abstractmethod
    def create_table(self, request):
        pass

    @abstractmethod
    def create_table_invoker(self, request):
        pass

    @abstractmethod
    def delete_table(self, request):
        pass

    @abstractmethod
    def delete_table_invoker(self, request):
        pass

    @abstractmethod
    def describe_table(self, request):
        pass

    @abstractmethod
    def describe_table_invoker(self, request):
        pass

    @abstractmethod
    def list_store(self, request):
        pass

    @abstractmethod
    def list_store_invoker(self, request):
        pass

    @abstractmethod
    def list_table(self, request):
        pass

    @abstractmethod
    def list_table_invoker(self, request):
        pass

    @abstractmethod
    def batch_get_kv(self, request):
        pass

    @abstractmethod
    def batch_get_kv_invoker(self, request):
        pass

    @abstractmethod
    def batch_write_kv(self, request):
        pass

    @abstractmethod
    def batch_write_kv_invoker(self, request):
        pass

    @abstractmethod
    def delete_kv(self, request):
        pass

    @abstractmethod
    def delete_kv_invoker(self, request):
        pass

    @abstractmethod
    def get_kv(self, request):
        pass

    @abstractmethod
    def get_kv_invoker(self, request):
        pass

    @abstractmethod
    def put_kv(self, request):
        pass

    @abstractmethod
    def put_kv_invoker(self, request):
        pass

    @abstractmethod
    def scan_kv(self, request):
        pass

    @abstractmethod
    def scan_kv_invoker(self, request):
        pass

    @abstractmethod
    def scan_skey_kv(self, request):
        pass

    @abstractmethod
    def scan_skey_kv_invoker(self, request):
        pass

    @abstractmethod
    def update_kv(self, request):
        pass

    @abstractmethod
    def update_kv_invoker(self, request):
        pass

    @abstractmethod
    def check_health(self, request):
        pass

    @abstractmethod
    def check_health_invoker(self, request):
        pass
