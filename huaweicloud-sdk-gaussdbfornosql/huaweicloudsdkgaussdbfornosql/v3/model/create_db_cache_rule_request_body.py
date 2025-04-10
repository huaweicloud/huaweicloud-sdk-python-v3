# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDbCacheRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dbcache_mapping_id': 'str',
        'name': 'str',
        'source_db_schema': 'str',
        'source_db_table': 'str',
        'storage_type': 'str',
        'target_database': 'str',
        'key_columns': 'list[str]',
        'value_columns': 'list[str]',
        'ttl': 'str',
        'key_separator': 'str',
        'value_separator': 'str',
        'key_prefix': 'str'
    }

    attribute_map = {
        'dbcache_mapping_id': 'dbcache_mapping_id',
        'name': 'name',
        'source_db_schema': 'source_db_schema',
        'source_db_table': 'source_db_table',
        'storage_type': 'storage_type',
        'target_database': 'target_database',
        'key_columns': 'key_columns',
        'value_columns': 'value_columns',
        'ttl': 'ttl',
        'key_separator': 'key_separator',
        'value_separator': 'value_separator',
        'key_prefix': 'key_prefix'
    }

    def __init__(self, dbcache_mapping_id=None, name=None, source_db_schema=None, source_db_table=None, storage_type=None, target_database=None, key_columns=None, value_columns=None, ttl=None, key_separator=None, value_separator=None, key_prefix=None):
        r"""CreateDbCacheRuleRequestBody

        The model defined in huaweicloud sdk

        :param dbcache_mapping_id: 内存加速映射ID。
        :type dbcache_mapping_id: str
        :param name: 内存加速规则名称。不超过256字符，需要确保在当前映射下唯一。
        :type name: str
        :param source_db_schema: 源端数据库。
        :type source_db_schema: str
        :param source_db_table: 源端数据表。
        :type source_db_table: str
        :param storage_type: 目标数据存储类型。 取值为： hash。
        :type storage_type: str
        :param target_database: 目标数据库。取值范围： [0-999]。
        :type target_database: str
        :param key_columns: 映射的key使用的column列表。
        :type key_columns: list[str]
        :param value_columns: 映射的value使用的column列表。
        :type value_columns: list[str]
        :param ttl: key的生存时间。单位:ms。不传该值，默认取2592000000，表示30天。
        :type ttl: str
        :param key_separator: 映射的key分隔符。只允许一个字符。
        :type key_separator: str
        :param value_separator: 映射的value分隔符。只允许一个字符。
        :type value_separator: str
        :param key_prefix: 键前缀。最长限制1024字符。需确保key_prefix和target_database在当前映射下唯一。
        :type key_prefix: str
        """
        
        

        self._dbcache_mapping_id = None
        self._name = None
        self._source_db_schema = None
        self._source_db_table = None
        self._storage_type = None
        self._target_database = None
        self._key_columns = None
        self._value_columns = None
        self._ttl = None
        self._key_separator = None
        self._value_separator = None
        self._key_prefix = None
        self.discriminator = None

        self.dbcache_mapping_id = dbcache_mapping_id
        self.name = name
        self.source_db_schema = source_db_schema
        self.source_db_table = source_db_table
        self.storage_type = storage_type
        self.target_database = target_database
        self.key_columns = key_columns
        self.value_columns = value_columns
        if ttl is not None:
            self.ttl = ttl
        self.key_separator = key_separator
        if value_separator is not None:
            self.value_separator = value_separator
        self.key_prefix = key_prefix

    @property
    def dbcache_mapping_id(self):
        r"""Gets the dbcache_mapping_id of this CreateDbCacheRuleRequestBody.

        内存加速映射ID。

        :return: The dbcache_mapping_id of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._dbcache_mapping_id

    @dbcache_mapping_id.setter
    def dbcache_mapping_id(self, dbcache_mapping_id):
        r"""Sets the dbcache_mapping_id of this CreateDbCacheRuleRequestBody.

        内存加速映射ID。

        :param dbcache_mapping_id: The dbcache_mapping_id of this CreateDbCacheRuleRequestBody.
        :type dbcache_mapping_id: str
        """
        self._dbcache_mapping_id = dbcache_mapping_id

    @property
    def name(self):
        r"""Gets the name of this CreateDbCacheRuleRequestBody.

        内存加速规则名称。不超过256字符，需要确保在当前映射下唯一。

        :return: The name of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateDbCacheRuleRequestBody.

        内存加速规则名称。不超过256字符，需要确保在当前映射下唯一。

        :param name: The name of this CreateDbCacheRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def source_db_schema(self):
        r"""Gets the source_db_schema of this CreateDbCacheRuleRequestBody.

        源端数据库。

        :return: The source_db_schema of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._source_db_schema

    @source_db_schema.setter
    def source_db_schema(self, source_db_schema):
        r"""Sets the source_db_schema of this CreateDbCacheRuleRequestBody.

        源端数据库。

        :param source_db_schema: The source_db_schema of this CreateDbCacheRuleRequestBody.
        :type source_db_schema: str
        """
        self._source_db_schema = source_db_schema

    @property
    def source_db_table(self):
        r"""Gets the source_db_table of this CreateDbCacheRuleRequestBody.

        源端数据表。

        :return: The source_db_table of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._source_db_table

    @source_db_table.setter
    def source_db_table(self, source_db_table):
        r"""Sets the source_db_table of this CreateDbCacheRuleRequestBody.

        源端数据表。

        :param source_db_table: The source_db_table of this CreateDbCacheRuleRequestBody.
        :type source_db_table: str
        """
        self._source_db_table = source_db_table

    @property
    def storage_type(self):
        r"""Gets the storage_type of this CreateDbCacheRuleRequestBody.

        目标数据存储类型。 取值为： hash。

        :return: The storage_type of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this CreateDbCacheRuleRequestBody.

        目标数据存储类型。 取值为： hash。

        :param storage_type: The storage_type of this CreateDbCacheRuleRequestBody.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def target_database(self):
        r"""Gets the target_database of this CreateDbCacheRuleRequestBody.

        目标数据库。取值范围： [0-999]。

        :return: The target_database of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._target_database

    @target_database.setter
    def target_database(self, target_database):
        r"""Sets the target_database of this CreateDbCacheRuleRequestBody.

        目标数据库。取值范围： [0-999]。

        :param target_database: The target_database of this CreateDbCacheRuleRequestBody.
        :type target_database: str
        """
        self._target_database = target_database

    @property
    def key_columns(self):
        r"""Gets the key_columns of this CreateDbCacheRuleRequestBody.

        映射的key使用的column列表。

        :return: The key_columns of this CreateDbCacheRuleRequestBody.
        :rtype: list[str]
        """
        return self._key_columns

    @key_columns.setter
    def key_columns(self, key_columns):
        r"""Sets the key_columns of this CreateDbCacheRuleRequestBody.

        映射的key使用的column列表。

        :param key_columns: The key_columns of this CreateDbCacheRuleRequestBody.
        :type key_columns: list[str]
        """
        self._key_columns = key_columns

    @property
    def value_columns(self):
        r"""Gets the value_columns of this CreateDbCacheRuleRequestBody.

        映射的value使用的column列表。

        :return: The value_columns of this CreateDbCacheRuleRequestBody.
        :rtype: list[str]
        """
        return self._value_columns

    @value_columns.setter
    def value_columns(self, value_columns):
        r"""Sets the value_columns of this CreateDbCacheRuleRequestBody.

        映射的value使用的column列表。

        :param value_columns: The value_columns of this CreateDbCacheRuleRequestBody.
        :type value_columns: list[str]
        """
        self._value_columns = value_columns

    @property
    def ttl(self):
        r"""Gets the ttl of this CreateDbCacheRuleRequestBody.

        key的生存时间。单位:ms。不传该值，默认取2592000000，表示30天。

        :return: The ttl of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this CreateDbCacheRuleRequestBody.

        key的生存时间。单位:ms。不传该值，默认取2592000000，表示30天。

        :param ttl: The ttl of this CreateDbCacheRuleRequestBody.
        :type ttl: str
        """
        self._ttl = ttl

    @property
    def key_separator(self):
        r"""Gets the key_separator of this CreateDbCacheRuleRequestBody.

        映射的key分隔符。只允许一个字符。

        :return: The key_separator of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._key_separator

    @key_separator.setter
    def key_separator(self, key_separator):
        r"""Sets the key_separator of this CreateDbCacheRuleRequestBody.

        映射的key分隔符。只允许一个字符。

        :param key_separator: The key_separator of this CreateDbCacheRuleRequestBody.
        :type key_separator: str
        """
        self._key_separator = key_separator

    @property
    def value_separator(self):
        r"""Gets the value_separator of this CreateDbCacheRuleRequestBody.

        映射的value分隔符。只允许一个字符。

        :return: The value_separator of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._value_separator

    @value_separator.setter
    def value_separator(self, value_separator):
        r"""Sets the value_separator of this CreateDbCacheRuleRequestBody.

        映射的value分隔符。只允许一个字符。

        :param value_separator: The value_separator of this CreateDbCacheRuleRequestBody.
        :type value_separator: str
        """
        self._value_separator = value_separator

    @property
    def key_prefix(self):
        r"""Gets the key_prefix of this CreateDbCacheRuleRequestBody.

        键前缀。最长限制1024字符。需确保key_prefix和target_database在当前映射下唯一。

        :return: The key_prefix of this CreateDbCacheRuleRequestBody.
        :rtype: str
        """
        return self._key_prefix

    @key_prefix.setter
    def key_prefix(self, key_prefix):
        r"""Sets the key_prefix of this CreateDbCacheRuleRequestBody.

        键前缀。最长限制1024字符。需确保key_prefix和target_database在当前映射下唯一。

        :param key_prefix: The key_prefix of this CreateDbCacheRuleRequestBody.
        :type key_prefix: str
        """
        self._key_prefix = key_prefix

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateDbCacheRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
