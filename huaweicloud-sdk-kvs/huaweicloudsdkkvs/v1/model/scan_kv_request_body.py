# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScanKvRequestBody:

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
        'start_key': 'dict',
        'end_key': 'dict',
        'filter_expression': 'ConditionExpression',
        'projection_fields': 'list[str]',
        'sample_segments_count': 'int',
        'return_count_only': 'bool'
    }

    attribute_map = {
        'table_name': 'table_name',
        'hint_index_name': 'hint_index_name',
        'limit': 'limit',
        'start_key': 'start_key',
        'end_key': 'end_key',
        'filter_expression': 'filter_expression',
        'projection_fields': 'projection_fields',
        'sample_segments_count': 'sample_segments_count',
        'return_count_only': 'return_count_only'
    }

    def __init__(self, table_name=None, hint_index_name=None, limit=None, start_key=None, end_key=None, filter_expression=None, projection_fields=None, sample_segments_count=None, return_count_only=None):
        r"""ScanKvRequestBody

        The model defined in huaweicloud sdk

        :param table_name: 表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+
        :type table_name: str
        :param hint_index_name: create_table时指定的索引名，默认空表示主索引。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+
        :type hint_index_name: str
        :param limit: 数据量不超过1MB时，返回的文档个数，最大100个，默认1MB或者100个文档。
        :type limit: int
        :param start_key: 起始主键或索引键值。 - 默认空，表示从头遍历，左闭。 &gt; 分页返回时，该值使用上次响应返回的cursor_key。
        :type start_key: dict
        :param end_key: 终止主键或索引键值。 - 默认空，表示直到最后，右开。
        :type end_key: dict
        :param filter_expression: 
        :type filter_expression: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        :param projection_fields: 对kv_doc有效，返回指定字段列表，默认全部。
        :type projection_fields: list[str]
        :param sample_segments_count: 对表进行采样，尽最大努力保证返回的段列表均分整张表。举例：sample_segments_count&#x3D;4，返回的段列表[MinKey, KV1)、[KV1,KV2)、[KV2,KV3)和[KV3,MaxKey)。用户可以使用scan-kv对这四个分区执行并发扫描，提高遍历效率。 - 范围: [1, 10000]。默认值：不执行采样。 - sample_segments_count仅能和table_name、start_key和end_key字段配合使用。Range分区模式下支持全表采样和范围采样；Hash分区模式仅支持全表扫描。 - 仅支持对Primary key进行采样，不支持本地/全局二级索引。 - 返回的段列表仅包含主键，不包含键值；且段列表是编码后的数据 ，不可修改。
        :type sample_segments_count: int
        :param return_count_only: 返回查询条件对应的KV总数. - 当KV总数小于limit条件时，返回KV查询结果和KV总数。 - 当KV总数多于limit条件时，只返回KV总数。
        :type return_count_only: bool
        """
        
        

        self._table_name = None
        self._hint_index_name = None
        self._limit = None
        self._start_key = None
        self._end_key = None
        self._filter_expression = None
        self._projection_fields = None
        self._sample_segments_count = None
        self._return_count_only = None
        self.discriminator = None

        self.table_name = table_name
        if hint_index_name is not None:
            self.hint_index_name = hint_index_name
        if limit is not None:
            self.limit = limit
        if start_key is not None:
            self.start_key = start_key
        if end_key is not None:
            self.end_key = end_key
        if filter_expression is not None:
            self.filter_expression = filter_expression
        if projection_fields is not None:
            self.projection_fields = projection_fields
        if sample_segments_count is not None:
            self.sample_segments_count = sample_segments_count
        if return_count_only is not None:
            self.return_count_only = return_count_only

    @property
    def table_name(self):
        r"""Gets the table_name of this ScanKvRequestBody.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :return: The table_name of this ScanKvRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ScanKvRequestBody.

        表名，仓内唯一。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :param table_name: The table_name of this ScanKvRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def hint_index_name(self):
        r"""Gets the hint_index_name of this ScanKvRequestBody.

        create_table时指定的索引名，默认空表示主索引。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :return: The hint_index_name of this ScanKvRequestBody.
        :rtype: str
        """
        return self._hint_index_name

    @hint_index_name.setter
    def hint_index_name(self, hint_index_name):
        r"""Sets the hint_index_name of this ScanKvRequestBody.

        create_table时指定的索引名，默认空表示主索引。 - 长度：[3, 63] - 取值字符限制：[a-z0-9_-]+

        :param hint_index_name: The hint_index_name of this ScanKvRequestBody.
        :type hint_index_name: str
        """
        self._hint_index_name = hint_index_name

    @property
    def limit(self):
        r"""Gets the limit of this ScanKvRequestBody.

        数据量不超过1MB时，返回的文档个数，最大100个，默认1MB或者100个文档。

        :return: The limit of this ScanKvRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ScanKvRequestBody.

        数据量不超过1MB时，返回的文档个数，最大100个，默认1MB或者100个文档。

        :param limit: The limit of this ScanKvRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_key(self):
        r"""Gets the start_key of this ScanKvRequestBody.

        起始主键或索引键值。 - 默认空，表示从头遍历，左闭。 > 分页返回时，该值使用上次响应返回的cursor_key。

        :return: The start_key of this ScanKvRequestBody.
        :rtype: dict
        """
        return self._start_key

    @start_key.setter
    def start_key(self, start_key):
        r"""Sets the start_key of this ScanKvRequestBody.

        起始主键或索引键值。 - 默认空，表示从头遍历，左闭。 > 分页返回时，该值使用上次响应返回的cursor_key。

        :param start_key: The start_key of this ScanKvRequestBody.
        :type start_key: dict
        """
        self._start_key = start_key

    @property
    def end_key(self):
        r"""Gets the end_key of this ScanKvRequestBody.

        终止主键或索引键值。 - 默认空，表示直到最后，右开。

        :return: The end_key of this ScanKvRequestBody.
        :rtype: dict
        """
        return self._end_key

    @end_key.setter
    def end_key(self, end_key):
        r"""Sets the end_key of this ScanKvRequestBody.

        终止主键或索引键值。 - 默认空，表示直到最后，右开。

        :param end_key: The end_key of this ScanKvRequestBody.
        :type end_key: dict
        """
        self._end_key = end_key

    @property
    def filter_expression(self):
        r"""Gets the filter_expression of this ScanKvRequestBody.

        :return: The filter_expression of this ScanKvRequestBody.
        :rtype: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        """
        return self._filter_expression

    @filter_expression.setter
    def filter_expression(self, filter_expression):
        r"""Sets the filter_expression of this ScanKvRequestBody.

        :param filter_expression: The filter_expression of this ScanKvRequestBody.
        :type filter_expression: :class:`huaweicloudsdkkvs.v1.ConditionExpression`
        """
        self._filter_expression = filter_expression

    @property
    def projection_fields(self):
        r"""Gets the projection_fields of this ScanKvRequestBody.

        对kv_doc有效，返回指定字段列表，默认全部。

        :return: The projection_fields of this ScanKvRequestBody.
        :rtype: list[str]
        """
        return self._projection_fields

    @projection_fields.setter
    def projection_fields(self, projection_fields):
        r"""Sets the projection_fields of this ScanKvRequestBody.

        对kv_doc有效，返回指定字段列表，默认全部。

        :param projection_fields: The projection_fields of this ScanKvRequestBody.
        :type projection_fields: list[str]
        """
        self._projection_fields = projection_fields

    @property
    def sample_segments_count(self):
        r"""Gets the sample_segments_count of this ScanKvRequestBody.

        对表进行采样，尽最大努力保证返回的段列表均分整张表。举例：sample_segments_count=4，返回的段列表[MinKey, KV1)、[KV1,KV2)、[KV2,KV3)和[KV3,MaxKey)。用户可以使用scan-kv对这四个分区执行并发扫描，提高遍历效率。 - 范围: [1, 10000]。默认值：不执行采样。 - sample_segments_count仅能和table_name、start_key和end_key字段配合使用。Range分区模式下支持全表采样和范围采样；Hash分区模式仅支持全表扫描。 - 仅支持对Primary key进行采样，不支持本地/全局二级索引。 - 返回的段列表仅包含主键，不包含键值；且段列表是编码后的数据 ，不可修改。

        :return: The sample_segments_count of this ScanKvRequestBody.
        :rtype: int
        """
        return self._sample_segments_count

    @sample_segments_count.setter
    def sample_segments_count(self, sample_segments_count):
        r"""Sets the sample_segments_count of this ScanKvRequestBody.

        对表进行采样，尽最大努力保证返回的段列表均分整张表。举例：sample_segments_count=4，返回的段列表[MinKey, KV1)、[KV1,KV2)、[KV2,KV3)和[KV3,MaxKey)。用户可以使用scan-kv对这四个分区执行并发扫描，提高遍历效率。 - 范围: [1, 10000]。默认值：不执行采样。 - sample_segments_count仅能和table_name、start_key和end_key字段配合使用。Range分区模式下支持全表采样和范围采样；Hash分区模式仅支持全表扫描。 - 仅支持对Primary key进行采样，不支持本地/全局二级索引。 - 返回的段列表仅包含主键，不包含键值；且段列表是编码后的数据 ，不可修改。

        :param sample_segments_count: The sample_segments_count of this ScanKvRequestBody.
        :type sample_segments_count: int
        """
        self._sample_segments_count = sample_segments_count

    @property
    def return_count_only(self):
        r"""Gets the return_count_only of this ScanKvRequestBody.

        返回查询条件对应的KV总数. - 当KV总数小于limit条件时，返回KV查询结果和KV总数。 - 当KV总数多于limit条件时，只返回KV总数。

        :return: The return_count_only of this ScanKvRequestBody.
        :rtype: bool
        """
        return self._return_count_only

    @return_count_only.setter
    def return_count_only(self, return_count_only):
        r"""Sets the return_count_only of this ScanKvRequestBody.

        返回查询条件对应的KV总数. - 当KV总数小于limit条件时，返回KV查询结果和KV总数。 - 当KV总数多于limit条件时，只返回KV总数。

        :param return_count_only: The return_count_only of this ScanKvRequestBody.
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
        if not isinstance(other, ScanKvRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
