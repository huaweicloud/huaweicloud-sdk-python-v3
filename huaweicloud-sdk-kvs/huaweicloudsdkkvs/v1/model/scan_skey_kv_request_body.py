# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScanSkeyKvRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'table_name': 'str',
        'hint_index_name': 'str',
        'limit': 'int',
        'shard_key': 'dict',
        'start_sort_key': 'dict',
        'end_sort_key': 'dict',
        'filter_expression': 'ConditionExpression',
        'return_count_only': 'bool'
    }

    attribute_map = {
        'table_name': 'table_name',
        'hint_index_name': 'hint_index_name',
        'limit': 'limit',
        'shard_key': 'shard_key',
        'start_sort_key': 'start_sort_key',
        'end_sort_key': 'end_sort_key',
        'filter_expression': 'filter_expression',
        'return_count_only': 'return_count_only'
    }

    def __init__(self, table_name=None, hint_index_name=None, limit=None, shard_key=None, start_sort_key=None, end_sort_key=None, filter_expression=None, return_count_only=None):
        r"""ScanSkeyKvRequestBody

        The model defined in huaweicloud sdk

        :param table_name: 表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+
        :type table_name: str
        :param hint_index_name: create_table时指定的索引名。
        :type hint_index_name: str
        :param limit: 数据量不超过1MB时，返回的文档个数，最大100个，默认1MB或者100个文档。
        :type limit: int
        :param shard_key: 要遍历的指定分区键下的kv。
        :type shard_key: dict
        :param start_sort_key: 起始排序键值，默认空表示从头遍历，左闭。 &gt; 分页返回时，该值使用上次响应返回的cursor_sort_key
        :type start_sort_key: dict
        :param end_sort_key: 终止主键或索引键值，默认空表示直到最后，右开。
        :type end_sort_key: dict
        :param filter_expression: 
        :type filter_expression: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        :param return_count_only: 返回查询条件对应的KV总数. - 当KV总数小于limit条件时，返回KV查询结果和KV总数。 - 当KV总数多于limit条件时，只返回KV总数。
        :type return_count_only: bool
        """
        
        

        self._table_name = None
        self._hint_index_name = None
        self._limit = None
        self._shard_key = None
        self._start_sort_key = None
        self._end_sort_key = None
        self._filter_expression = None
        self._return_count_only = None
        self.discriminator = None

        self.table_name = table_name
        if hint_index_name is not None:
            self.hint_index_name = hint_index_name
        if limit is not None:
            self.limit = limit
        self.shard_key = shard_key
        if start_sort_key is not None:
            self.start_sort_key = start_sort_key
        if end_sort_key is not None:
            self.end_sort_key = end_sort_key
        if filter_expression is not None:
            self.filter_expression = filter_expression
        if return_count_only is not None:
            self.return_count_only = return_count_only

    @property
    def table_name(self):
        r"""Gets the table_name of this ScanSkeyKvRequestBody.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :return: The table_name of this ScanSkeyKvRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ScanSkeyKvRequestBody.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :param table_name: The table_name of this ScanSkeyKvRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def hint_index_name(self):
        r"""Gets the hint_index_name of this ScanSkeyKvRequestBody.

        create_table时指定的索引名。

        :return: The hint_index_name of this ScanSkeyKvRequestBody.
        :rtype: str
        """
        return self._hint_index_name

    @hint_index_name.setter
    def hint_index_name(self, hint_index_name):
        r"""Sets the hint_index_name of this ScanSkeyKvRequestBody.

        create_table时指定的索引名。

        :param hint_index_name: The hint_index_name of this ScanSkeyKvRequestBody.
        :type hint_index_name: str
        """
        self._hint_index_name = hint_index_name

    @property
    def limit(self):
        r"""Gets the limit of this ScanSkeyKvRequestBody.

        数据量不超过1MB时，返回的文档个数，最大100个，默认1MB或者100个文档。

        :return: The limit of this ScanSkeyKvRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ScanSkeyKvRequestBody.

        数据量不超过1MB时，返回的文档个数，最大100个，默认1MB或者100个文档。

        :param limit: The limit of this ScanSkeyKvRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def shard_key(self):
        r"""Gets the shard_key of this ScanSkeyKvRequestBody.

        要遍历的指定分区键下的kv。

        :return: The shard_key of this ScanSkeyKvRequestBody.
        :rtype: dict
        """
        return self._shard_key

    @shard_key.setter
    def shard_key(self, shard_key):
        r"""Sets the shard_key of this ScanSkeyKvRequestBody.

        要遍历的指定分区键下的kv。

        :param shard_key: The shard_key of this ScanSkeyKvRequestBody.
        :type shard_key: dict
        """
        self._shard_key = shard_key

    @property
    def start_sort_key(self):
        r"""Gets the start_sort_key of this ScanSkeyKvRequestBody.

        起始排序键值，默认空表示从头遍历，左闭。 > 分页返回时，该值使用上次响应返回的cursor_sort_key

        :return: The start_sort_key of this ScanSkeyKvRequestBody.
        :rtype: dict
        """
        return self._start_sort_key

    @start_sort_key.setter
    def start_sort_key(self, start_sort_key):
        r"""Sets the start_sort_key of this ScanSkeyKvRequestBody.

        起始排序键值，默认空表示从头遍历，左闭。 > 分页返回时，该值使用上次响应返回的cursor_sort_key

        :param start_sort_key: The start_sort_key of this ScanSkeyKvRequestBody.
        :type start_sort_key: dict
        """
        self._start_sort_key = start_sort_key

    @property
    def end_sort_key(self):
        r"""Gets the end_sort_key of this ScanSkeyKvRequestBody.

        终止主键或索引键值，默认空表示直到最后，右开。

        :return: The end_sort_key of this ScanSkeyKvRequestBody.
        :rtype: dict
        """
        return self._end_sort_key

    @end_sort_key.setter
    def end_sort_key(self, end_sort_key):
        r"""Sets the end_sort_key of this ScanSkeyKvRequestBody.

        终止主键或索引键值，默认空表示直到最后，右开。

        :param end_sort_key: The end_sort_key of this ScanSkeyKvRequestBody.
        :type end_sort_key: dict
        """
        self._end_sort_key = end_sort_key

    @property
    def filter_expression(self):
        r"""Gets the filter_expression of this ScanSkeyKvRequestBody.

        :return: The filter_expression of this ScanSkeyKvRequestBody.
        :rtype: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        """
        return self._filter_expression

    @filter_expression.setter
    def filter_expression(self, filter_expression):
        r"""Sets the filter_expression of this ScanSkeyKvRequestBody.

        :param filter_expression: The filter_expression of this ScanSkeyKvRequestBody.
        :type filter_expression: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        """
        self._filter_expression = filter_expression

    @property
    def return_count_only(self):
        r"""Gets the return_count_only of this ScanSkeyKvRequestBody.

        返回查询条件对应的KV总数. - 当KV总数小于limit条件时，返回KV查询结果和KV总数。 - 当KV总数多于limit条件时，只返回KV总数。

        :return: The return_count_only of this ScanSkeyKvRequestBody.
        :rtype: bool
        """
        return self._return_count_only

    @return_count_only.setter
    def return_count_only(self, return_count_only):
        r"""Sets the return_count_only of this ScanSkeyKvRequestBody.

        返回查询条件对应的KV总数. - 当KV总数小于limit条件时，返回KV查询结果和KV总数。 - 当KV总数多于limit条件时，只返回KV总数。

        :param return_count_only: The return_count_only of this ScanSkeyKvRequestBody.
        :type return_count_only: bool
        """
        self._return_count_only = return_count_only

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
        if not isinstance(other, ScanSkeyKvRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
