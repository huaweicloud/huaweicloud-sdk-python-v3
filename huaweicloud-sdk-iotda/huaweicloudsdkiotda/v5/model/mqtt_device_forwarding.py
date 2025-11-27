# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MqttDeviceForwarding:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'topic': 'topic',
        'ttl': 'ttl'
    }

    def __init__(self, topic=None, ttl=None):
        r"""MqttDeviceForwarding

        The model defined in huaweicloud sdk

        :param topic: **参数说明**：消息重发布topic
        :type topic: str
        :param ttl: **参数说明**：消息重发布过期时间，单位为分钟
        :type ttl: int
        """
        
        

        self._topic = None
        self._ttl = None
        self.discriminator = None

        self.topic = topic
        if ttl is not None:
            self.ttl = ttl

    @property
    def topic(self):
        r"""Gets the topic of this MqttDeviceForwarding.

        **参数说明**：消息重发布topic

        :return: The topic of this MqttDeviceForwarding.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        r"""Sets the topic of this MqttDeviceForwarding.

        **参数说明**：消息重发布topic

        :param topic: The topic of this MqttDeviceForwarding.
        :type topic: str
        """
        self._topic = topic

    @property
    def ttl(self):
        r"""Gets the ttl of this MqttDeviceForwarding.

        **参数说明**：消息重发布过期时间，单位为分钟

        :return: The ttl of this MqttDeviceForwarding.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        r"""Sets the ttl of this MqttDeviceForwarding.

        **参数说明**：消息重发布过期时间，单位为分钟

        :param ttl: The ttl of this MqttDeviceForwarding.
        :type ttl: int
        """
        self._ttl = ttl

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MqttDeviceForwarding):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
