# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpeedLimitlJson:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start': 'str',
        'end': 'str',
        'speed': 'int'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end',
        'speed': 'speed'
    }

    def __init__(self, start=None, end=None, speed=None):
        """SpeedLimitlJson

        The model defined in huaweicloud sdk

        :param start: 时间段开始时间，格式：XX:XX。
        :type start: str
        :param end: 时间段结束时间，格式：XX:XX。
        :type end: str
        :param speed: 时间段的速率，0-1000的整数，单位：Mbit/s。
        :type speed: int
        """
        
        

        self._start = None
        self._end = None
        self._speed = None
        self.discriminator = None

        self.start = start
        self.end = end
        self.speed = speed

    @property
    def start(self):
        """Gets the start of this SpeedLimitlJson.

        时间段开始时间，格式：XX:XX。

        :return: The start of this SpeedLimitlJson.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this SpeedLimitlJson.

        时间段开始时间，格式：XX:XX。

        :param start: The start of this SpeedLimitlJson.
        :type start: str
        """
        self._start = start

    @property
    def end(self):
        """Gets the end of this SpeedLimitlJson.

        时间段结束时间，格式：XX:XX。

        :return: The end of this SpeedLimitlJson.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this SpeedLimitlJson.

        时间段结束时间，格式：XX:XX。

        :param end: The end of this SpeedLimitlJson.
        :type end: str
        """
        self._end = end

    @property
    def speed(self):
        """Gets the speed of this SpeedLimitlJson.

        时间段的速率，0-1000的整数，单位：Mbit/s。

        :return: The speed of this SpeedLimitlJson.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this SpeedLimitlJson.

        时间段的速率，0-1000的整数，单位：Mbit/s。

        :param speed: The speed of this SpeedLimitlJson.
        :type speed: int
        """
        self._speed = speed

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
        if not isinstance(other, SpeedLimitlJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
