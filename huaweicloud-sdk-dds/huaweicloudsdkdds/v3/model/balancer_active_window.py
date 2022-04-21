# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BalancerActiveWindow:

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
        'stop_time': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'stop_time': 'stop_time'
    }

    def __init__(self, start_time=None, stop_time=None):
        """BalancerActiveWindow

        The model defined in huaweicloud sdk

        :param start_time: 活动时间窗开始时间。
        :type start_time: str
        :param stop_time: 活动时间窗结束时间。
        :type stop_time: str
        """
        
        

        self._start_time = None
        self._stop_time = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if stop_time is not None:
            self.stop_time = stop_time

    @property
    def start_time(self):
        """Gets the start_time of this BalancerActiveWindow.

        活动时间窗开始时间。

        :return: The start_time of this BalancerActiveWindow.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this BalancerActiveWindow.

        活动时间窗开始时间。

        :param start_time: The start_time of this BalancerActiveWindow.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def stop_time(self):
        """Gets the stop_time of this BalancerActiveWindow.

        活动时间窗结束时间。

        :return: The stop_time of this BalancerActiveWindow.
        :rtype: str
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this BalancerActiveWindow.

        活动时间窗结束时间。

        :param stop_time: The stop_time of this BalancerActiveWindow.
        :type stop_time: str
        """
        self._stop_time = stop_time

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
        if not isinstance(other, BalancerActiveWindow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
