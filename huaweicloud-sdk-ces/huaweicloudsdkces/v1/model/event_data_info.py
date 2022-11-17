# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventDataInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'timestamp': 'int',
        'value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'timestamp': 'timestamp',
        'value': 'value'
    }

    def __init__(self, type=None, timestamp=None, value=None):
        """EventDataInfo

        The model defined in huaweicloud sdk

        :param type: 事件类型，例如instance_host_info。
        :type type: str
        :param timestamp: 事件上报时间。
        :type timestamp: int
        :param value: 主机配置信息。
        :type value: str
        """
        
        

        self._type = None
        self._timestamp = None
        self._value = None
        self.discriminator = None

        self.type = type
        self.timestamp = timestamp
        self.value = value

    @property
    def type(self):
        """Gets the type of this EventDataInfo.

        事件类型，例如instance_host_info。

        :return: The type of this EventDataInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventDataInfo.

        事件类型，例如instance_host_info。

        :param type: The type of this EventDataInfo.
        :type type: str
        """
        self._type = type

    @property
    def timestamp(self):
        """Gets the timestamp of this EventDataInfo.

        事件上报时间。

        :return: The timestamp of this EventDataInfo.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this EventDataInfo.

        事件上报时间。

        :param timestamp: The timestamp of this EventDataInfo.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def value(self):
        """Gets the value of this EventDataInfo.

        主机配置信息。

        :return: The value of this EventDataInfo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EventDataInfo.

        主机配置信息。

        :param value: The value of this EventDataInfo.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, EventDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
