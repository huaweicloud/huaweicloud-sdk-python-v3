# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryUserSelectedObjectInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'schema_name': 'str',
        'table_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'has_column_info': 'bool'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name',
        'offset': 'offset',
        'limit': 'limit',
        'has_column_info': 'has_column_info'
    }

    def __init__(self, db_name=None, schema_name=None, table_name=None, offset=None, limit=None, has_column_info=None):
        """QueryUserSelectedObjectInfoReq

        The model defined in huaweicloud sdk

        :param db_name: 库名。
        :type db_name: str
        :param schema_name: 模式名。
        :type schema_name: str
        :param table_name: 表名。
        :type table_name: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0
        :type offset: int
        :param limit: 每页显示的条目数量。默认为10，取值范围【1-1000】
        :type limit: int
        :param has_column_info: 是否有映射。
        :type has_column_info: bool
        """
        
        

        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self._offset = None
        self._limit = None
        self._has_column_info = None
        self.discriminator = None

        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if has_column_info is not None:
            self.has_column_info = has_column_info

    @property
    def db_name(self):
        """Gets the db_name of this QueryUserSelectedObjectInfoReq.

        库名。

        :return: The db_name of this QueryUserSelectedObjectInfoReq.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this QueryUserSelectedObjectInfoReq.

        库名。

        :param db_name: The db_name of this QueryUserSelectedObjectInfoReq.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        """Gets the schema_name of this QueryUserSelectedObjectInfoReq.

        模式名。

        :return: The schema_name of this QueryUserSelectedObjectInfoReq.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this QueryUserSelectedObjectInfoReq.

        模式名。

        :param schema_name: The schema_name of this QueryUserSelectedObjectInfoReq.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this QueryUserSelectedObjectInfoReq.

        表名。

        :return: The table_name of this QueryUserSelectedObjectInfoReq.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this QueryUserSelectedObjectInfoReq.

        表名。

        :param table_name: The table_name of this QueryUserSelectedObjectInfoReq.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def offset(self):
        """Gets the offset of this QueryUserSelectedObjectInfoReq.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :return: The offset of this QueryUserSelectedObjectInfoReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueryUserSelectedObjectInfoReq.

        偏移量，表示从此偏移量开始查询， offset 大于等于 0。默认为0

        :param offset: The offset of this QueryUserSelectedObjectInfoReq.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QueryUserSelectedObjectInfoReq.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :return: The limit of this QueryUserSelectedObjectInfoReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueryUserSelectedObjectInfoReq.

        每页显示的条目数量。默认为10，取值范围【1-1000】

        :param limit: The limit of this QueryUserSelectedObjectInfoReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def has_column_info(self):
        """Gets the has_column_info of this QueryUserSelectedObjectInfoReq.

        是否有映射。

        :return: The has_column_info of this QueryUserSelectedObjectInfoReq.
        :rtype: bool
        """
        return self._has_column_info

    @has_column_info.setter
    def has_column_info(self, has_column_info):
        """Sets the has_column_info of this QueryUserSelectedObjectInfoReq.

        是否有映射。

        :param has_column_info: The has_column_info of this QueryUserSelectedObjectInfoReq.
        :type has_column_info: bool
        """
        self._has_column_info = has_column_info

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
        if not isinstance(other, QueryUserSelectedObjectInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
