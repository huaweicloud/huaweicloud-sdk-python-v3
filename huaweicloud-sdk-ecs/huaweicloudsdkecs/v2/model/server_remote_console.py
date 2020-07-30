# coding: utf-8

import pprint
import re

import six





class ServerRemoteConsole:


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
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, protocol=None, type=None, url=None):
        """ServerRemoteConsole - a model defined in huaweicloud sdk"""
        
        

        self._protocol = None
        self._type = None
        self._url = None
        self.discriminator = None

        self.protocol = protocol
        self.type = type
        self.url = url

    @property
    def protocol(self):
        """Gets the protocol of this ServerRemoteConsole.

        远程登录的协议。

        :return: The protocol of this ServerRemoteConsole.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ServerRemoteConsole.

        远程登录的协议。

        :param protocol: The protocol of this ServerRemoteConsole.
        :type: str
        """
        self._protocol = protocol

    @property
    def type(self):
        """Gets the type of this ServerRemoteConsole.

        远程登录的类型。

        :return: The type of this ServerRemoteConsole.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServerRemoteConsole.

        远程登录的类型。

        :param type: The type of this ServerRemoteConsole.
        :type: str
        """
        self._type = type

    @property
    def url(self):
        """Gets the url of this ServerRemoteConsole.

        远程登录的url。

        :return: The url of this ServerRemoteConsole.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ServerRemoteConsole.

        远程登录的url。

        :param url: The url of this ServerRemoteConsole.
        :type: str
        """
        self._url = url

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerRemoteConsole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
