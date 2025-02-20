# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse


class GetKvResponse(SdkResponse):
    sensitive_list = []

    openapi_types = {
        'kv_doc': 'dict'
    }

    attribute_map = {
        'kv_doc': 'kv_doc'
    }

    def __init__(self, kv_doc=None):
        super(GetKvResponse, self).__init__()

        self._kv_doc = None
        self.discriminator = None

        if kv_doc is not None:
            self.kv_doc = kv_doc


class GetKvRequest(object):
    openapi_types = {
        'table_name': 'test-table',
        'primary_key': 'dict',
    }

    attribute_map = {
        'table_name': 'table_name',
        'primary_key': 'primary_key',
    }

    def __init__(self, table_name=None, primary_key=None):
        self.table_name = table_name
        self.primary_key = primary_key


class BsonBody(object):
    openapi_types = {
        'doc_field': 'dict',
        'binary_field': 'bytes',
        'min_key_field': 'MinKey',
        'max_key_field': 'MaxKey',
        'regex_field': 'Regex',
        'object_id_field': 'ObjectId',
        'js_code_field': 'Code'
    }

    attribute_map = {
        'doc_field': 'doc_field',
        'binary_field': 'binary_field',
        'min_key_field': 'min_key_field',
        'max_key_field': 'max_key_field',
        'regex_field': 'regex_field',
        'object_id_field': 'object_id_field',
        'js_code_field': 'js_code_field'
    }

    def __init__(self, doc_field=None, binary_field=None, min_key_field=None, max_key_field=None, regex_field=None,
                 object_id_field=None, js_code_field=None):
        self.doc_field = None
        self.binary_field = None
        self.min_key_field = None
        self.max_key_field = None
        self.regex_field = None
        self.object_id_field = None
        self.js_code_field = None

        if doc_field is not None:
            self.doc_field = doc_field
        if binary_field is not None:
            self.binary_field = binary_field
        if min_key_field is not None:
            self.min_key_field = min_key_field
        if max_key_field is not None:
            self.max_key_field = max_key_field
        if regex_field is not None:
            self.regex_field = regex_field
        if object_id_field is not None:
            self.object_id_field = object_id_field
        if js_code_field is not None:
            self.js_code_field = js_code_field
