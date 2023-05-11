# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowLogStatisticsForLtsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int',
        'type': 'str',
        'database': 'str',
        'sort': 'str',
        'order': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'database': 'database',
        'sort': 'sort',
        'order': 'order'
    }

    def __init__(self, start_time=None, end_time=None, offset=None, limit=None, type=None, database=None, sort=None, order=None):
        """SlowLogStatisticsForLtsRequest

        The model defined in huaweicloud sdk

        :param start_time: 开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。
        :type end_time: str
        :param offset: 索引位置，偏移量。默认为0，表示从第一条数据开始查询。
        :type offset: int
        :param limit: 每页多少条记录（查询结果），取值范围是1~100，不填时默认为10。
        :type limit: int
        :param type: 语句类型，取空值，表示查询所有语句类型。
        :type type: str
        :param database: 数据库名称。
        :type database: str
        :param sort: 指定排序字段。\&quot;executeTime\&quot;，表示按照执行时间降序排序。字段为空或传入其他值，表示按照执行次数降序排序。
        :type sort: str
        :param order: 排序顺序。默认desc。
        :type order: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self._type = None
        self._database = None
        self._sort = None
        self._order = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type
        if database is not None:
            self.database = database
        if sort is not None:
            self.sort = sort
        if order is not None:
            self.order = order

    @property
    def start_time(self):
        """Gets the start_time of this SlowLogStatisticsForLtsRequest.

        开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_time of this SlowLogStatisticsForLtsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SlowLogStatisticsForLtsRequest.

        开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_time: The start_time of this SlowLogStatisticsForLtsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this SlowLogStatisticsForLtsRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。

        :return: The end_time of this SlowLogStatisticsForLtsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SlowLogStatisticsForLtsRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。

        :param end_time: The end_time of this SlowLogStatisticsForLtsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        """Gets the offset of this SlowLogStatisticsForLtsRequest.

        索引位置，偏移量。默认为0，表示从第一条数据开始查询。

        :return: The offset of this SlowLogStatisticsForLtsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SlowLogStatisticsForLtsRequest.

        索引位置，偏移量。默认为0，表示从第一条数据开始查询。

        :param offset: The offset of this SlowLogStatisticsForLtsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SlowLogStatisticsForLtsRequest.

        每页多少条记录（查询结果），取值范围是1~100，不填时默认为10。

        :return: The limit of this SlowLogStatisticsForLtsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SlowLogStatisticsForLtsRequest.

        每页多少条记录（查询结果），取值范围是1~100，不填时默认为10。

        :param limit: The limit of this SlowLogStatisticsForLtsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this SlowLogStatisticsForLtsRequest.

        语句类型，取空值，表示查询所有语句类型。

        :return: The type of this SlowLogStatisticsForLtsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SlowLogStatisticsForLtsRequest.

        语句类型，取空值，表示查询所有语句类型。

        :param type: The type of this SlowLogStatisticsForLtsRequest.
        :type type: str
        """
        self._type = type

    @property
    def database(self):
        """Gets the database of this SlowLogStatisticsForLtsRequest.

        数据库名称。

        :return: The database of this SlowLogStatisticsForLtsRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SlowLogStatisticsForLtsRequest.

        数据库名称。

        :param database: The database of this SlowLogStatisticsForLtsRequest.
        :type database: str
        """
        self._database = database

    @property
    def sort(self):
        """Gets the sort of this SlowLogStatisticsForLtsRequest.

        指定排序字段。\"executeTime\"，表示按照执行时间降序排序。字段为空或传入其他值，表示按照执行次数降序排序。

        :return: The sort of this SlowLogStatisticsForLtsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this SlowLogStatisticsForLtsRequest.

        指定排序字段。\"executeTime\"，表示按照执行时间降序排序。字段为空或传入其他值，表示按照执行次数降序排序。

        :param sort: The sort of this SlowLogStatisticsForLtsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def order(self):
        """Gets the order of this SlowLogStatisticsForLtsRequest.

        排序顺序。默认desc。

        :return: The order of this SlowLogStatisticsForLtsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this SlowLogStatisticsForLtsRequest.

        排序顺序。默认desc。

        :param order: The order of this SlowLogStatisticsForLtsRequest.
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
        if not isinstance(other, SlowLogStatisticsForLtsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
