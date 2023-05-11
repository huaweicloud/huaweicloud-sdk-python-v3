# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeLineItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'int',
        'num': 'int'
    }

    attribute_map = {
        'time': 'time',
        'num': 'num'
    }

    def __init__(self, time=None, num=None):
        """TimeLineItem

        The model defined in huaweicloud sdk

        :param time: 时间点
        :type time: int
        :param num: 数量
        :type num: int
        """
        
        

        self._time = None
        self._num = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if num is not None:
            self.num = num

    @property
    def time(self):
        """Gets the time of this TimeLineItem.

        时间点

        :return: The time of this TimeLineItem.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this TimeLineItem.

        时间点

        :param time: The time of this TimeLineItem.
        :type time: int
        """
        self._time = time

    @property
    def num(self):
        """Gets the num of this TimeLineItem.

        数量

        :return: The num of this TimeLineItem.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this TimeLineItem.

        数量

        :param num: The num of this TimeLineItem.
        :type num: int
        """
        self._num = num

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
        if not isinstance(other, TimeLineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
