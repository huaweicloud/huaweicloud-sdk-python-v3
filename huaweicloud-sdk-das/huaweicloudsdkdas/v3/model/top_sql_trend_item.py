# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopSqlTrendItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execute_at': 'int',
        'query_time_in_100ms': 'int',
        'query_time_in_500ms': 'int',
        'query_time_in_1s': 'int',
        'query_time_over_1s': 'int'
    }

    attribute_map = {
        'execute_at': 'execute_at',
        'query_time_in_100ms': 'query_time_in_100ms',
        'query_time_in_500ms': 'query_time_in_500ms',
        'query_time_in_1s': 'query_time_in_1s',
        'query_time_over_1s': 'query_time_over_1s'
    }

    def __init__(self, execute_at=None, query_time_in_100ms=None, query_time_in_500ms=None, query_time_in_1s=None, query_time_over_1s=None):
        """TopSqlTrendItem

        The model defined in huaweicloud sdk

        :param execute_at: 执行时间点，毫秒时间戳。表示统计数据的时间范围为execute_at - interval_millis到execute_at。
        :type execute_at: int
        :param query_time_in_100ms: 执行耗时小于100ms。
        :type query_time_in_100ms: int
        :param query_time_in_500ms: 执行耗时100ms-500ms。
        :type query_time_in_500ms: int
        :param query_time_in_1s: 执行耗时500ms-1000ms
        :type query_time_in_1s: int
        :param query_time_over_1s: 执行耗时大于1000ms。
        :type query_time_over_1s: int
        """
        
        

        self._execute_at = None
        self._query_time_in_100ms = None
        self._query_time_in_500ms = None
        self._query_time_in_1s = None
        self._query_time_over_1s = None
        self.discriminator = None

        self.execute_at = execute_at
        self.query_time_in_100ms = query_time_in_100ms
        self.query_time_in_500ms = query_time_in_500ms
        self.query_time_in_1s = query_time_in_1s
        self.query_time_over_1s = query_time_over_1s

    @property
    def execute_at(self):
        """Gets the execute_at of this TopSqlTrendItem.

        执行时间点，毫秒时间戳。表示统计数据的时间范围为execute_at - interval_millis到execute_at。

        :return: The execute_at of this TopSqlTrendItem.
        :rtype: int
        """
        return self._execute_at

    @execute_at.setter
    def execute_at(self, execute_at):
        """Sets the execute_at of this TopSqlTrendItem.

        执行时间点，毫秒时间戳。表示统计数据的时间范围为execute_at - interval_millis到execute_at。

        :param execute_at: The execute_at of this TopSqlTrendItem.
        :type execute_at: int
        """
        self._execute_at = execute_at

    @property
    def query_time_in_100ms(self):
        """Gets the query_time_in_100ms of this TopSqlTrendItem.

        执行耗时小于100ms。

        :return: The query_time_in_100ms of this TopSqlTrendItem.
        :rtype: int
        """
        return self._query_time_in_100ms

    @query_time_in_100ms.setter
    def query_time_in_100ms(self, query_time_in_100ms):
        """Sets the query_time_in_100ms of this TopSqlTrendItem.

        执行耗时小于100ms。

        :param query_time_in_100ms: The query_time_in_100ms of this TopSqlTrendItem.
        :type query_time_in_100ms: int
        """
        self._query_time_in_100ms = query_time_in_100ms

    @property
    def query_time_in_500ms(self):
        """Gets the query_time_in_500ms of this TopSqlTrendItem.

        执行耗时100ms-500ms。

        :return: The query_time_in_500ms of this TopSqlTrendItem.
        :rtype: int
        """
        return self._query_time_in_500ms

    @query_time_in_500ms.setter
    def query_time_in_500ms(self, query_time_in_500ms):
        """Sets the query_time_in_500ms of this TopSqlTrendItem.

        执行耗时100ms-500ms。

        :param query_time_in_500ms: The query_time_in_500ms of this TopSqlTrendItem.
        :type query_time_in_500ms: int
        """
        self._query_time_in_500ms = query_time_in_500ms

    @property
    def query_time_in_1s(self):
        """Gets the query_time_in_1s of this TopSqlTrendItem.

        执行耗时500ms-1000ms

        :return: The query_time_in_1s of this TopSqlTrendItem.
        :rtype: int
        """
        return self._query_time_in_1s

    @query_time_in_1s.setter
    def query_time_in_1s(self, query_time_in_1s):
        """Sets the query_time_in_1s of this TopSqlTrendItem.

        执行耗时500ms-1000ms

        :param query_time_in_1s: The query_time_in_1s of this TopSqlTrendItem.
        :type query_time_in_1s: int
        """
        self._query_time_in_1s = query_time_in_1s

    @property
    def query_time_over_1s(self):
        """Gets the query_time_over_1s of this TopSqlTrendItem.

        执行耗时大于1000ms。

        :return: The query_time_over_1s of this TopSqlTrendItem.
        :rtype: int
        """
        return self._query_time_over_1s

    @query_time_over_1s.setter
    def query_time_over_1s(self, query_time_over_1s):
        """Sets the query_time_over_1s of this TopSqlTrendItem.

        执行耗时大于1000ms。

        :param query_time_over_1s: The query_time_over_1s of this TopSqlTrendItem.
        :type query_time_over_1s: int
        """
        self._query_time_over_1s = query_time_over_1s

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
        if not isinstance(other, TopSqlTrendItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
