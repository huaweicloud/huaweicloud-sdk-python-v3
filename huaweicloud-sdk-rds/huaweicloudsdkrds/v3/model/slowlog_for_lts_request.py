# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowlogForLtsRequest:

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
        'type': 'str',
        'line_num': 'str',
        'limit': 'int',
        'search_type': 'str',
        'database': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'type': 'type',
        'line_num': 'line_num',
        'limit': 'limit',
        'search_type': 'search_type',
        'database': 'database'
    }

    def __init__(self, start_time=None, end_time=None, type=None, line_num=None, limit=None, search_type=None, database=None):
        """SlowlogForLtsRequest

        The model defined in huaweicloud sdk

        :param start_time: 开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_time: str
        :param end_time: 结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。
        :type end_time: str
        :param type: 语句类型，取空值，表示查询所有语句类型。
        :type type: str
        :param line_num: 日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。line_num应在start_time和end_time之间。
        :type line_num: str
        :param limit: 每页多少条记录（查询结果），取值范围是1~100，不填时默认为10。
        :type limit: int
        :param search_type: 搜索方式。默认forwards。配合line_num使用，以line_num为起点，向前搜索或向后搜索。
        :type search_type: str
        :param database: 数据库名称。
        :type database: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._type = None
        self._line_num = None
        self._limit = None
        self._search_type = None
        self._database = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if type is not None:
            self.type = type
        if line_num is not None:
            self.line_num = line_num
        if limit is not None:
            self.limit = limit
        if search_type is not None:
            self.search_type = search_type
        if database is not None:
            self.database = database

    @property
    def start_time(self):
        """Gets the start_time of this SlowlogForLtsRequest.

        开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_time of this SlowlogForLtsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SlowlogForLtsRequest.

        开始日期，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_time: The start_time of this SlowlogForLtsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this SlowlogForLtsRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。

        :return: The end_time of this SlowlogForLtsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SlowlogForLtsRequest.

        结束时间，格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。只能查询当前时间前一个月内的慢日志。

        :param end_time: The end_time of this SlowlogForLtsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def type(self):
        """Gets the type of this SlowlogForLtsRequest.

        语句类型，取空值，表示查询所有语句类型。

        :return: The type of this SlowlogForLtsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SlowlogForLtsRequest.

        语句类型，取空值，表示查询所有语句类型。

        :param type: The type of this SlowlogForLtsRequest.
        :type type: str
        """
        self._type = type

    @property
    def line_num(self):
        """Gets the line_num of this SlowlogForLtsRequest.

        日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。line_num应在start_time和end_time之间。

        :return: The line_num of this SlowlogForLtsRequest.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        """Sets the line_num of this SlowlogForLtsRequest.

        日志单行序列号，第一次查询时不需要此参数，后续分页查询时需要使用，可从上次查询的返回信息中获取。line_num应在start_time和end_time之间。

        :param line_num: The line_num of this SlowlogForLtsRequest.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def limit(self):
        """Gets the limit of this SlowlogForLtsRequest.

        每页多少条记录（查询结果），取值范围是1~100，不填时默认为10。

        :return: The limit of this SlowlogForLtsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SlowlogForLtsRequest.

        每页多少条记录（查询结果），取值范围是1~100，不填时默认为10。

        :param limit: The limit of this SlowlogForLtsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search_type(self):
        """Gets the search_type of this SlowlogForLtsRequest.

        搜索方式。默认forwards。配合line_num使用，以line_num为起点，向前搜索或向后搜索。

        :return: The search_type of this SlowlogForLtsRequest.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """Sets the search_type of this SlowlogForLtsRequest.

        搜索方式。默认forwards。配合line_num使用，以line_num为起点，向前搜索或向后搜索。

        :param search_type: The search_type of this SlowlogForLtsRequest.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def database(self):
        """Gets the database of this SlowlogForLtsRequest.

        数据库名称。

        :return: The database of this SlowlogForLtsRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SlowlogForLtsRequest.

        数据库名称。

        :param database: The database of this SlowlogForLtsRequest.
        :type database: str
        """
        self._database = database

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
        if not isinstance(other, SlowlogForLtsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
