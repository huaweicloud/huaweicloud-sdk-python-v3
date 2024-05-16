# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportSlowSqlStatisticsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datastore_type': 'str',
        'start_at': 'int',
        'end_at': 'int',
        'node_ids': 'list[str]',
        'statistics_field': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'datastore_type': 'datastore_type',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'node_ids': 'node_ids',
        'statistics_field': 'statistics_field',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, datastore_type=None, start_at=None, end_at=None, node_ids=None, statistics_field=None, offset=None, limit=None):
        """ExportSlowSqlStatisticsRequestBody

        The model defined in huaweicloud sdk

        :param datastore_type: 数据库类型。慢SQL统计支持的类型：DDS-Community。
        :type datastore_type: str
        :param start_at: 开始时间（Unix timestamp），单位：毫秒。
        :type start_at: int
        :param end_at: 结束时间（Unix timestamp），单位：毫秒。
        :type end_at: int
        :param node_ids: 节点ID列表。
        :type node_ids: list[str]
        :param statistics_field: 统计字段。支持统计的字段：node_id、sql_type、db_name、collection、user、client。默认使用node_id统计。
        :type statistics_field: str
        :param offset: 偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 每页记录数，默认为20，最大取值100。
        :type limit: int
        """
        
        

        self._datastore_type = None
        self._start_at = None
        self._end_at = None
        self._node_ids = None
        self._statistics_field = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.datastore_type = datastore_type
        self.start_at = start_at
        self.end_at = end_at
        if node_ids is not None:
            self.node_ids = node_ids
        if statistics_field is not None:
            self.statistics_field = statistics_field
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def datastore_type(self):
        """Gets the datastore_type of this ExportSlowSqlStatisticsRequestBody.

        数据库类型。慢SQL统计支持的类型：DDS-Community。

        :return: The datastore_type of this ExportSlowSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        """Sets the datastore_type of this ExportSlowSqlStatisticsRequestBody.

        数据库类型。慢SQL统计支持的类型：DDS-Community。

        :param datastore_type: The datastore_type of this ExportSlowSqlStatisticsRequestBody.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def start_at(self):
        """Gets the start_at of this ExportSlowSqlStatisticsRequestBody.

        开始时间（Unix timestamp），单位：毫秒。

        :return: The start_at of this ExportSlowSqlStatisticsRequestBody.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        """Sets the start_at of this ExportSlowSqlStatisticsRequestBody.

        开始时间（Unix timestamp），单位：毫秒。

        :param start_at: The start_at of this ExportSlowSqlStatisticsRequestBody.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        """Gets the end_at of this ExportSlowSqlStatisticsRequestBody.

        结束时间（Unix timestamp），单位：毫秒。

        :return: The end_at of this ExportSlowSqlStatisticsRequestBody.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this ExportSlowSqlStatisticsRequestBody.

        结束时间（Unix timestamp），单位：毫秒。

        :param end_at: The end_at of this ExportSlowSqlStatisticsRequestBody.
        :type end_at: int
        """
        self._end_at = end_at

    @property
    def node_ids(self):
        """Gets the node_ids of this ExportSlowSqlStatisticsRequestBody.

        节点ID列表。

        :return: The node_ids of this ExportSlowSqlStatisticsRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this ExportSlowSqlStatisticsRequestBody.

        节点ID列表。

        :param node_ids: The node_ids of this ExportSlowSqlStatisticsRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def statistics_field(self):
        """Gets the statistics_field of this ExportSlowSqlStatisticsRequestBody.

        统计字段。支持统计的字段：node_id、sql_type、db_name、collection、user、client。默认使用node_id统计。

        :return: The statistics_field of this ExportSlowSqlStatisticsRequestBody.
        :rtype: str
        """
        return self._statistics_field

    @statistics_field.setter
    def statistics_field(self, statistics_field):
        """Sets the statistics_field of this ExportSlowSqlStatisticsRequestBody.

        统计字段。支持统计的字段：node_id、sql_type、db_name、collection、user、client。默认使用node_id统计。

        :param statistics_field: The statistics_field of this ExportSlowSqlStatisticsRequestBody.
        :type statistics_field: str
        """
        self._statistics_field = statistics_field

    @property
    def offset(self):
        """Gets the offset of this ExportSlowSqlStatisticsRequestBody.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ExportSlowSqlStatisticsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ExportSlowSqlStatisticsRequestBody.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ExportSlowSqlStatisticsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ExportSlowSqlStatisticsRequestBody.

        每页记录数，默认为20，最大取值100。

        :return: The limit of this ExportSlowSqlStatisticsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ExportSlowSqlStatisticsRequestBody.

        每页记录数，默认为20，最大取值100。

        :param limit: The limit of this ExportSlowSqlStatisticsRequestBody.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ExportSlowSqlStatisticsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
