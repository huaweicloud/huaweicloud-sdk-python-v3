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
        'js_code_field': 'Code',
        'string_field': 'str',  # 字符串
        'int32_field': 'int',  # 32位整数
        'int64_field': 'int',  # 64位整数（Python中int类型即可）
        'double_field': 'float',  # 浮点数
        'decimal128_field': 'Decimal128',  # 高精度 Decimal128
        'boolean_field': 'bool',  # 布尔值
        'null_field': 'NoneType',  # 空值
        'array_field': 'list',  # 数组
        'timestamp_field': 'Timestamp'  # 时间戳
    }

    attribute_map = {
        'doc_field': 'doc_field',
        'binary_field': 'binary_field',
        'min_key_field': 'min_key_field',
        'max_key_field': 'max_key_field',
        'regex_field': 'regex_field',
        'object_id_field': 'object_id_field',
        'js_code_field': 'js_code_field',
        'string_field': 'string_field',
        'int32_field': 'int32_field',
        'int64_field': 'int64_field',
        'double_field': 'double_field',
        'decimal128_field': 'decimal128_field',
        'boolean_field': 'boolean_field',
        'null_field': 'null_field',
        'array_field': 'array_field',
        'timestamp_field': 'timestamp_field'
    }

    def __init__(self,
                 doc_field=None,
                 binary_field=None,
                 min_key_field=None,
                 max_key_field=None,
                 regex_field=None,
                 object_id_field=None,
                 js_code_field=None,
                 string_field=None,
                 int32_field=None,
                 int64_field=None,
                 double_field=None,
                 decimal128_field=None,
                 boolean_field=None,
                 null_field=None,
                 array_field=None,
                 timestamp_field=None):

        # 初始化所有字段为 None
        self.doc_field = None
        self.binary_field = None
        self.min_key_field = None
        self.max_key_field = None
        self.regex_field = None
        self.object_id_field = None
        self.js_code_field = None
        self.string_field = None
        self.int32_field = None
        self.int64_field = None
        self.double_field = None
        self.decimal128_field = None
        self.boolean_field = None
        self.null_field = None
        self.array_field = None
        self.timestamp_field = None

        # 根据传入的参数赋值
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
        if string_field is not None:
            self.string_field = string_field
        if int32_field is not None:
            self.int32_field = int32_field
        if int64_field is not None:
            self.int64_field = int64_field
        if double_field is not None:
            self.double_field = double_field
        if decimal128_field is not None:
            self.decimal128_field = decimal128_field
        if boolean_field is not None:
            self.boolean_field = boolean_field
        if null_field is not None:
            self.null_field = null_field
        if array_field is not None:
            self.array_field = array_field
        if timestamp_field is not None:
            self.timestamp_field = timestamp_field
