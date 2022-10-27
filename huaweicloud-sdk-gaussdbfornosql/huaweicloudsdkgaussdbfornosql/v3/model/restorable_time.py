# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestorableTime:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, start_time=None, end_time=None):
        """RestorableTime

        The model defined in huaweicloud sdk

        :param start_time: 可恢复时间段的开始时间点，UNIX时间戳格式，单位是毫秒，时区是UTC。
        :type start_time: int
        :param end_time: 可恢复时间段的结束时间点， UNIX时间戳格式，单位是毫秒，时区是UTC。
        :type end_time: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time

    @property
    def start_time(self):
        """Gets the start_time of this RestorableTime.

        可恢复时间段的开始时间点，UNIX时间戳格式，单位是毫秒，时区是UTC。

        :return: The start_time of this RestorableTime.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RestorableTime.

        可恢复时间段的开始时间点，UNIX时间戳格式，单位是毫秒，时区是UTC。

        :param start_time: The start_time of this RestorableTime.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this RestorableTime.

        可恢复时间段的结束时间点， UNIX时间戳格式，单位是毫秒，时区是UTC。

        :return: The end_time of this RestorableTime.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RestorableTime.

        可恢复时间段的结束时间点， UNIX时间戳格式，单位是毫秒，时区是UTC。

        :param end_time: The end_time of this RestorableTime.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, RestorableTime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
