# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyEventRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'name': 'str',
        'event_type': 'str'
    }

    attribute_map = {
        'time': 'time',
        'name': 'name',
        'event_type': 'event_type'
    }

    def __init__(self, time=None, name=None, event_type=None):
        """PolicyEventRsp

        The model defined in huaweicloud sdk

        :param time: 事件产生时间
        :type time: str
        :param name: 事件名称
        :type name: str
        :param event_type: 事件类型
        :type event_type: str
        """
        
        

        self._time = None
        self._name = None
        self._event_type = None
        self.discriminator = None

        self.time = time
        self.name = name
        self.event_type = event_type

    @property
    def time(self):
        """Gets the time of this PolicyEventRsp.

        事件产生时间

        :return: The time of this PolicyEventRsp.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this PolicyEventRsp.

        事件产生时间

        :param time: The time of this PolicyEventRsp.
        :type time: str
        """
        self._time = time

    @property
    def name(self):
        """Gets the name of this PolicyEventRsp.

        事件名称

        :return: The name of this PolicyEventRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyEventRsp.

        事件名称

        :param name: The name of this PolicyEventRsp.
        :type name: str
        """
        self._name = name

    @property
    def event_type(self):
        """Gets the event_type of this PolicyEventRsp.

        事件类型

        :return: The event_type of this PolicyEventRsp.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PolicyEventRsp.

        事件类型

        :param event_type: The event_type of this PolicyEventRsp.
        :type event_type: str
        """
        self._event_type = event_type

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
        if not isinstance(other, PolicyEventRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
