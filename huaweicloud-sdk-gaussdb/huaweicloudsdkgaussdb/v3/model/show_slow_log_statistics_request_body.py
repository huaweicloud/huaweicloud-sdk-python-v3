# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSlowLogStatisticsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'node_id': 'str',
        'type': 'str',
        'database': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'sort': 'str',
        'order': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'node_id': 'node_id',
        'type': 'type',
        'database': 'database',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'sort': 'sort',
        'order': 'order'
    }

    def __init__(self, limit=None, offset=None, node_id=None, type=None, database=None, start_time=None, end_time=None, sort=None, order=None):
        r"""ShowSlowLogStatisticsRequestBody

        The model defined in huaweicloud sdk

        :param limit: 每页多少条记录（查询结果），取值范围是1~100，不填时默认为10。
        :type limit: int
        :param offset: 索引位置，偏移量。默认为0，表示从第一条数据开始查询。
        :type offset: int
        :param node_id: 节点ID。
        :type node_id: str
        :param type: 语句类型，取空值，表示查询所有语句类型。  枚举值:   - INSERT   - UPDATE   - SELECT   - DELETE   - CREATE   - ALL
        :type type: str
        :param database: 数据库名称。数据库名称不支持包含特殊字符 &lt; &gt; &amp; 等的搜索。
        :type database: str
        :param start_time: 开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。
        :type end_time: str
        :param sort: 指定排序字段。   - executeTime：表示按照平均执行时间降序排序。   - 字段为空或传入其他值，表示按照执行次数降序排序。
        :type sort: str
        :param order: 排序顺序。默认desc。 枚举值：   - desc   - asc
        :type order: str
        """
        
        

        self._limit = None
        self._offset = None
        self._node_id = None
        self._type = None
        self._database = None
        self._start_time = None
        self._end_time = None
        self._sort = None
        self._order = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.node_id = node_id
        if type is not None:
            self.type = type
        if database is not None:
            self.database = database
        self.start_time = start_time
        self.end_time = end_time
        if sort is not None:
            self.sort = sort
        if order is not None:
            self.order = order

    @property
    def limit(self):
        r"""Gets the limit of this ShowSlowLogStatisticsRequestBody.

        每页多少条记录（查询结果），取值范围是1~100，不填时默认为10。

        :return: The limit of this ShowSlowLogStatisticsRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowSlowLogStatisticsRequestBody.

        每页多少条记录（查询结果），取值范围是1~100，不填时默认为10。

        :param limit: The limit of this ShowSlowLogStatisticsRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowSlowLogStatisticsRequestBody.

        索引位置，偏移量。默认为0，表示从第一条数据开始查询。

        :return: The offset of this ShowSlowLogStatisticsRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowSlowLogStatisticsRequestBody.

        索引位置，偏移量。默认为0，表示从第一条数据开始查询。

        :param offset: The offset of this ShowSlowLogStatisticsRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowSlowLogStatisticsRequestBody.

        节点ID。

        :return: The node_id of this ShowSlowLogStatisticsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowSlowLogStatisticsRequestBody.

        节点ID。

        :param node_id: The node_id of this ShowSlowLogStatisticsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def type(self):
        r"""Gets the type of this ShowSlowLogStatisticsRequestBody.

        语句类型，取空值，表示查询所有语句类型。  枚举值:   - INSERT   - UPDATE   - SELECT   - DELETE   - CREATE   - ALL

        :return: The type of this ShowSlowLogStatisticsRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowSlowLogStatisticsRequestBody.

        语句类型，取空值，表示查询所有语句类型。  枚举值:   - INSERT   - UPDATE   - SELECT   - DELETE   - CREATE   - ALL

        :param type: The type of this ShowSlowLogStatisticsRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def database(self):
        r"""Gets the database of this ShowSlowLogStatisticsRequestBody.

        数据库名称。数据库名称不支持包含特殊字符 < > & 等的搜索。

        :return: The database of this ShowSlowLogStatisticsRequestBody.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ShowSlowLogStatisticsRequestBody.

        数据库名称。数据库名称不支持包含特殊字符 < > & 等的搜索。

        :param database: The database of this ShowSlowLogStatisticsRequestBody.
        :type database: str
        """
        self._database = database

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowSlowLogStatisticsRequestBody.

        开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_time of this ShowSlowLogStatisticsRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowSlowLogStatisticsRequestBody.

        开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_time: The start_time of this ShowSlowLogStatisticsRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowSlowLogStatisticsRequestBody.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。

        :return: The end_time of this ShowSlowLogStatisticsRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowSlowLogStatisticsRequestBody.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。  其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。

        :param end_time: The end_time of this ShowSlowLogStatisticsRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def sort(self):
        r"""Gets the sort of this ShowSlowLogStatisticsRequestBody.

        指定排序字段。   - executeTime：表示按照平均执行时间降序排序。   - 字段为空或传入其他值，表示按照执行次数降序排序。

        :return: The sort of this ShowSlowLogStatisticsRequestBody.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ShowSlowLogStatisticsRequestBody.

        指定排序字段。   - executeTime：表示按照平均执行时间降序排序。   - 字段为空或传入其他值，表示按照执行次数降序排序。

        :param sort: The sort of this ShowSlowLogStatisticsRequestBody.
        :type sort: str
        """
        self._sort = sort

    @property
    def order(self):
        r"""Gets the order of this ShowSlowLogStatisticsRequestBody.

        排序顺序。默认desc。 枚举值：   - desc   - asc

        :return: The order of this ShowSlowLogStatisticsRequestBody.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ShowSlowLogStatisticsRequestBody.

        排序顺序。默认desc。 枚举值：   - desc   - asc

        :param order: The order of this ShowSlowLogStatisticsRequestBody.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ShowSlowLogStatisticsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
