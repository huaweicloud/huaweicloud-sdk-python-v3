# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchWindow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'time': 'int',
        'interval': 'int'
    }

    attribute_map = {
        'count': 'count',
        'time': 'time',
        'interval': 'interval'
    }

    def __init__(self, count=None, time=None, interval=None):
        r"""BatchWindow

        The model defined in huaweicloud sdk

        :param count: 批量推送条数[1,10000]
        :type count: int
        :param time: 重试次数
        :type time: int
        :param interval: 批量推送间隔[0,15]，单位秒
        :type interval: int
        """
        
        

        self._count = None
        self._time = None
        self._interval = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if time is not None:
            self.time = time
        if interval is not None:
            self.interval = interval

    @property
    def count(self):
        r"""Gets the count of this BatchWindow.

        批量推送条数[1,10000]

        :return: The count of this BatchWindow.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this BatchWindow.

        批量推送条数[1,10000]

        :param count: The count of this BatchWindow.
        :type count: int
        """
        self._count = count

    @property
    def time(self):
        r"""Gets the time of this BatchWindow.

        重试次数

        :return: The time of this BatchWindow.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this BatchWindow.

        重试次数

        :param time: The time of this BatchWindow.
        :type time: int
        """
        self._time = time

    @property
    def interval(self):
        r"""Gets the interval of this BatchWindow.

        批量推送间隔[0,15]，单位秒

        :return: The interval of this BatchWindow.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        r"""Sets the interval of this BatchWindow.

        批量推送间隔[0,15]，单位秒

        :param interval: The interval of this BatchWindow.
        :type interval: int
        """
        self._interval = interval

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
        if not isinstance(other, BatchWindow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
