# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventResponseSource:

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
        'host_scheduled_event_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'host_scheduled_event_id': 'host_scheduled_event_id'
    }

    def __init__(self, type=None, host_scheduled_event_id=None):
        r"""EventResponseSource

        The model defined in huaweicloud sdk

        :param type: 计划事件来源类型
        :type type: str
        :param host_scheduled_event_id: 主机计划事件ID
        :type host_scheduled_event_id: str
        """
        
        

        self._type = None
        self._host_scheduled_event_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if host_scheduled_event_id is not None:
            self.host_scheduled_event_id = host_scheduled_event_id

    @property
    def type(self):
        r"""Gets the type of this EventResponseSource.

        计划事件来源类型

        :return: The type of this EventResponseSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EventResponseSource.

        计划事件来源类型

        :param type: The type of this EventResponseSource.
        :type type: str
        """
        self._type = type

    @property
    def host_scheduled_event_id(self):
        r"""Gets the host_scheduled_event_id of this EventResponseSource.

        主机计划事件ID

        :return: The host_scheduled_event_id of this EventResponseSource.
        :rtype: str
        """
        return self._host_scheduled_event_id

    @host_scheduled_event_id.setter
    def host_scheduled_event_id(self, host_scheduled_event_id):
        r"""Sets the host_scheduled_event_id of this EventResponseSource.

        主机计划事件ID

        :param host_scheduled_event_id: The host_scheduled_event_id of this EventResponseSource.
        :type host_scheduled_event_id: str
        """
        self._host_scheduled_event_id = host_scheduled_event_id

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
        if not isinstance(other, EventResponseSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
