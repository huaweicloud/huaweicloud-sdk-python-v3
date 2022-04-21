# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventSeries:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'event_severity': 'str',
        'values': 'list[int]'
    }

    attribute_map = {
        'event_severity': 'event_severity',
        'values': 'values'
    }

    def __init__(self, event_severity=None, values=None):
        """EventSeries

        The model defined in huaweicloud sdk

        :param event_severity: 事件或者告警级别枚举类型。
        :type event_severity: str
        :param values: 事件或者告警统计结果。
        :type values: list[int]
        """
        
        

        self._event_severity = None
        self._values = None
        self.discriminator = None

        if event_severity is not None:
            self.event_severity = event_severity
        if values is not None:
            self.values = values

    @property
    def event_severity(self):
        """Gets the event_severity of this EventSeries.

        事件或者告警级别枚举类型。

        :return: The event_severity of this EventSeries.
        :rtype: str
        """
        return self._event_severity

    @event_severity.setter
    def event_severity(self, event_severity):
        """Sets the event_severity of this EventSeries.

        事件或者告警级别枚举类型。

        :param event_severity: The event_severity of this EventSeries.
        :type event_severity: str
        """
        self._event_severity = event_severity

    @property
    def values(self):
        """Gets the values of this EventSeries.

        事件或者告警统计结果。

        :return: The values of this EventSeries.
        :rtype: list[int]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this EventSeries.

        事件或者告警统计结果。

        :param values: The values of this EventSeries.
        :type values: list[int]
        """
        self._values = values

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
        if not isinstance(other, EventSeries):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
