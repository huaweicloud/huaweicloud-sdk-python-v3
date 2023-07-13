# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetServerRemoteConsoleOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'type': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'type': 'type'
    }

    def __init__(self, protocol=None, type=None):
        """GetServerRemoteConsoleOption

        The model defined in huaweicloud sdk

        :param protocol: 远程登录协议，请将protocol配置为“vnc”。
        :type protocol: str
        :param type: 远程登录的类型，请将type配置为“novnc”。
        :type type: str
        """
        
        

        self._protocol = None
        self._type = None
        self.discriminator = None

        self.protocol = protocol
        self.type = type

    @property
    def protocol(self):
        """Gets the protocol of this GetServerRemoteConsoleOption.

        远程登录协议，请将protocol配置为“vnc”。

        :return: The protocol of this GetServerRemoteConsoleOption.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this GetServerRemoteConsoleOption.

        远程登录协议，请将protocol配置为“vnc”。

        :param protocol: The protocol of this GetServerRemoteConsoleOption.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def type(self):
        """Gets the type of this GetServerRemoteConsoleOption.

        远程登录的类型，请将type配置为“novnc”。

        :return: The type of this GetServerRemoteConsoleOption.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetServerRemoteConsoleOption.

        远程登录的类型，请将type配置为“novnc”。

        :param type: The type of this GetServerRemoteConsoleOption.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, GetServerRemoteConsoleOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
