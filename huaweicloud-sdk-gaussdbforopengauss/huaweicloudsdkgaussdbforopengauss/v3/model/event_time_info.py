# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventTimeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'events': 'list[TopEventInfoResult]',
        'left_time': 'int',
        'other_time': 'int'
    }

    attribute_map = {
        'events': 'events',
        'left_time': 'left_time',
        'other_time': 'other_time'
    }

    def __init__(self, events=None, left_time=None, other_time=None):
        r"""EventTimeInfo

        The model defined in huaweicloud sdk

        :param events: **参数解释**: TOP5事件耗时信息列表。
        :type events: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TopEventInfoResult`]
        :param left_time: **参数解释**: 其余事件耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type left_time: int
        :param other_time: **参数解释**: 事件外耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type other_time: int
        """
        
        

        self._events = None
        self._left_time = None
        self._other_time = None
        self.discriminator = None

        self.events = events
        self.left_time = left_time
        self.other_time = other_time

    @property
    def events(self):
        r"""Gets the events of this EventTimeInfo.

        **参数解释**: TOP5事件耗时信息列表。

        :return: The events of this EventTimeInfo.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TopEventInfoResult`]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this EventTimeInfo.

        **参数解释**: TOP5事件耗时信息列表。

        :param events: The events of this EventTimeInfo.
        :type events: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.TopEventInfoResult`]
        """
        self._events = events

    @property
    def left_time(self):
        r"""Gets the left_time of this EventTimeInfo.

        **参数解释**: 其余事件耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The left_time of this EventTimeInfo.
        :rtype: int
        """
        return self._left_time

    @left_time.setter
    def left_time(self, left_time):
        r"""Sets the left_time of this EventTimeInfo.

        **参数解释**: 其余事件耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param left_time: The left_time of this EventTimeInfo.
        :type left_time: int
        """
        self._left_time = left_time

    @property
    def other_time(self):
        r"""Gets the other_time of this EventTimeInfo.

        **参数解释**: 事件外耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The other_time of this EventTimeInfo.
        :rtype: int
        """
        return self._other_time

    @other_time.setter
    def other_time(self, other_time):
        r"""Sets the other_time of this EventTimeInfo.

        **参数解释**: 事件外耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param other_time: The other_time of this EventTimeInfo.
        :type other_time: int
        """
        self._other_time = other_time

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
        if not isinstance(other, EventTimeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
