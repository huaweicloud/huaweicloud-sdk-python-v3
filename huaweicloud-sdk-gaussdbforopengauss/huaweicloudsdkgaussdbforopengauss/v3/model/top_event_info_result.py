# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopEventInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_name': 'str',
        'event_time': 'int'
    }

    attribute_map = {
        'event_name': 'event_name',
        'event_time': 'event_time'
    }

    def __init__(self, event_name=None, event_time=None):
        r"""TopEventInfoResult

        The model defined in huaweicloud sdk

        :param event_name: **参数解释**: 事件名。 **取值范围**: 不涉及。
        :type event_name: str
        :param event_time: **参数解释**: 事件耗时（单位：微秒）。 **取值范围**: 不涉及。
        :type event_time: int
        """
        
        

        self._event_name = None
        self._event_time = None
        self.discriminator = None

        self.event_name = event_name
        self.event_time = event_time

    @property
    def event_name(self):
        r"""Gets the event_name of this TopEventInfoResult.

        **参数解释**: 事件名。 **取值范围**: 不涉及。

        :return: The event_name of this TopEventInfoResult.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this TopEventInfoResult.

        **参数解释**: 事件名。 **取值范围**: 不涉及。

        :param event_name: The event_name of this TopEventInfoResult.
        :type event_name: str
        """
        self._event_name = event_name

    @property
    def event_time(self):
        r"""Gets the event_time of this TopEventInfoResult.

        **参数解释**: 事件耗时（单位：微秒）。 **取值范围**: 不涉及。

        :return: The event_time of this TopEventInfoResult.
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        r"""Sets the event_time of this TopEventInfoResult.

        **参数解释**: 事件耗时（单位：微秒）。 **取值范围**: 不涉及。

        :param event_time: The event_time of this TopEventInfoResult.
        :type event_time: int
        """
        self._event_time = event_time

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
        if not isinstance(other, TopEventInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
