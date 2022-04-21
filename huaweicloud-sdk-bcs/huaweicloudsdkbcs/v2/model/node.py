# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Node:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'ip_port': 'str',
        'channels': 'list[str]'
    }

    attribute_map = {
        'ip_port': 'ip_port',
        'channels': 'channels'
    }

    def __init__(self, ip_port=None, channels=None):
        """Node

        The model defined in huaweicloud sdk

        :param ip_port: 节点EIP信息
        :type ip_port: str
        :param channels: 节点所在通道数组
        :type channels: list[str]
        """
        
        

        self._ip_port = None
        self._channels = None
        self.discriminator = None

        if ip_port is not None:
            self.ip_port = ip_port
        if channels is not None:
            self.channels = channels

    @property
    def ip_port(self):
        """Gets the ip_port of this Node.

        节点EIP信息

        :return: The ip_port of this Node.
        :rtype: str
        """
        return self._ip_port

    @ip_port.setter
    def ip_port(self, ip_port):
        """Sets the ip_port of this Node.

        节点EIP信息

        :param ip_port: The ip_port of this Node.
        :type ip_port: str
        """
        self._ip_port = ip_port

    @property
    def channels(self):
        """Gets the channels of this Node.

        节点所在通道数组

        :return: The channels of this Node.
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this Node.

        节点所在通道数组

        :param channels: The channels of this Node.
        :type channels: list[str]
        """
        self._channels = channels

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
        if not isinstance(other, Node):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
