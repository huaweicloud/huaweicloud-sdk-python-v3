# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlowSqlTrendItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestamp': 'int',
        'slow_log_count': 'int'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'slow_log_count': 'slow_log_count'
    }

    def __init__(self, timestamp=None, slow_log_count=None):
        r"""SlowSqlTrendItem

        The model defined in huaweicloud sdk

        :param timestamp: 毫秒时间戳。表示统计数据的时间范围为timestamp到timestamp + interval_millis。
        :type timestamp: int
        :param slow_log_count: 慢SQL数量。
        :type slow_log_count: int
        """
        
        

        self._timestamp = None
        self._slow_log_count = None
        self.discriminator = None

        self.timestamp = timestamp
        self.slow_log_count = slow_log_count

    @property
    def timestamp(self):
        r"""Gets the timestamp of this SlowSqlTrendItem.

        毫秒时间戳。表示统计数据的时间范围为timestamp到timestamp + interval_millis。

        :return: The timestamp of this SlowSqlTrendItem.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this SlowSqlTrendItem.

        毫秒时间戳。表示统计数据的时间范围为timestamp到timestamp + interval_millis。

        :param timestamp: The timestamp of this SlowSqlTrendItem.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def slow_log_count(self):
        r"""Gets the slow_log_count of this SlowSqlTrendItem.

        慢SQL数量。

        :return: The slow_log_count of this SlowSqlTrendItem.
        :rtype: int
        """
        return self._slow_log_count

    @slow_log_count.setter
    def slow_log_count(self, slow_log_count):
        r"""Sets the slow_log_count of this SlowSqlTrendItem.

        慢SQL数量。

        :param slow_log_count: The slow_log_count of this SlowSqlTrendItem.
        :type slow_log_count: int
        """
        self._slow_log_count = slow_log_count

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
        if not isinstance(other, SlowSqlTrendItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
