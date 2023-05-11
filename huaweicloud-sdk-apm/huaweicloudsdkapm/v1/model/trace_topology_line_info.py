# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TraceTopologyLineInfo:

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
        'time_used': 'int',
        'argument': 'str',
        'event_id': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'time_used': 'time_used',
        'argument': 'argument',
        'event_id': 'event_id'
    }

    def __init__(self, start_time=None, time_used=None, argument=None, event_id=None):
        """TraceTopologyLineInfo

        The model defined in huaweicloud sdk

        :param start_time: 开始时间。
        :type start_time: int
        :param time_used: 耗时。
        :type time_used: int
        :param argument: 参数信息，比如调用的url信息等。
        :type argument: str
        :param event_id: event的id。
        :type event_id: str
        """
        
        

        self._start_time = None
        self._time_used = None
        self._argument = None
        self._event_id = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if time_used is not None:
            self.time_used = time_used
        if argument is not None:
            self.argument = argument
        if event_id is not None:
            self.event_id = event_id

    @property
    def start_time(self):
        """Gets the start_time of this TraceTopologyLineInfo.

        开始时间。

        :return: The start_time of this TraceTopologyLineInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TraceTopologyLineInfo.

        开始时间。

        :param start_time: The start_time of this TraceTopologyLineInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def time_used(self):
        """Gets the time_used of this TraceTopologyLineInfo.

        耗时。

        :return: The time_used of this TraceTopologyLineInfo.
        :rtype: int
        """
        return self._time_used

    @time_used.setter
    def time_used(self, time_used):
        """Sets the time_used of this TraceTopologyLineInfo.

        耗时。

        :param time_used: The time_used of this TraceTopologyLineInfo.
        :type time_used: int
        """
        self._time_used = time_used

    @property
    def argument(self):
        """Gets the argument of this TraceTopologyLineInfo.

        参数信息，比如调用的url信息等。

        :return: The argument of this TraceTopologyLineInfo.
        :rtype: str
        """
        return self._argument

    @argument.setter
    def argument(self, argument):
        """Sets the argument of this TraceTopologyLineInfo.

        参数信息，比如调用的url信息等。

        :param argument: The argument of this TraceTopologyLineInfo.
        :type argument: str
        """
        self._argument = argument

    @property
    def event_id(self):
        """Gets the event_id of this TraceTopologyLineInfo.

        event的id。

        :return: The event_id of this TraceTopologyLineInfo.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this TraceTopologyLineInfo.

        event的id。

        :param event_id: The event_id of this TraceTopologyLineInfo.
        :type event_id: str
        """
        self._event_id = event_id

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
        if not isinstance(other, TraceTopologyLineInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
