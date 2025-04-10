# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeRange:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_type': 'str',
        'start': 'str',
        'end': 'str'
    }

    attribute_map = {
        'time_type': 'time_type',
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, time_type=None, start=None, end=None):
        r"""TimeRange

        The model defined in huaweicloud sdk

        :param time_type: 可选值：ddlUpdateTime、dataUpdateTime、ddlCreateTime
        :type time_type: str
        :param start: 开始时间
        :type start: str
        :param end: 结束时间
        :type end: str
        """
        
        

        self._time_type = None
        self._start = None
        self._end = None
        self.discriminator = None

        self.time_type = time_type
        self.start = start
        self.end = end

    @property
    def time_type(self):
        r"""Gets the time_type of this TimeRange.

        可选值：ddlUpdateTime、dataUpdateTime、ddlCreateTime

        :return: The time_type of this TimeRange.
        :rtype: str
        """
        return self._time_type

    @time_type.setter
    def time_type(self, time_type):
        r"""Sets the time_type of this TimeRange.

        可选值：ddlUpdateTime、dataUpdateTime、ddlCreateTime

        :param time_type: The time_type of this TimeRange.
        :type time_type: str
        """
        self._time_type = time_type

    @property
    def start(self):
        r"""Gets the start of this TimeRange.

        开始时间

        :return: The start of this TimeRange.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this TimeRange.

        开始时间

        :param start: The start of this TimeRange.
        :type start: str
        """
        self._start = start

    @property
    def end(self):
        r"""Gets the end of this TimeRange.

        结束时间

        :return: The end of this TimeRange.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this TimeRange.

        结束时间

        :param end: The end of this TimeRange.
        :type end: str
        """
        self._end = end

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
        if not isinstance(other, TimeRange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
