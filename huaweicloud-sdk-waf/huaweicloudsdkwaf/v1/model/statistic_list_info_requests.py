# coding: utf-8

import re
import six





class StatisticListInfoRequests:


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
        """StatisticListInfoRequests - a model defined in huaweicloud sdk"""
        
        

        self._time = None
        self._num = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if num is not None:
            self.num = num

    @property
    def time(self):
        """Gets the time of this StatisticListInfoRequests.

        统计终止时间点

        :return: The time of this StatisticListInfoRequests.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StatisticListInfoRequests.

        统计终止时间点

        :param time: The time of this StatisticListInfoRequests.
        :type: int
        """
        self._time = time

    @property
    def num(self):
        """Gets the num of this StatisticListInfoRequests.

        统计计数

        :return: The num of this StatisticListInfoRequests.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this StatisticListInfoRequests.

        统计计数

        :param num: The num of this StatisticListInfoRequests.
        :type: int
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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StatisticListInfoRequests):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
