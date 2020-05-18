# coding: utf-8

import pprint
import re

import six


class NovaVncConsole(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'url': 'str',
        'type': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'url': 'url',
        'type': 'type',
        'protocol': 'protocol'
    }

    def __init__(self, url=None, type=None, protocol=None):  # noqa: E501
        """NovaVncConsole - a model defined in huaweicloud sdk"""

        self._url = None
        self._type = None
        self._protocol = None
        self.discriminator = None

        self.url = url
        self.type = type
        if protocol is not None:
            self.protocol = protocol

    @property
    def url(self):
        """Gets the url of this NovaVncConsole.

        远程登录的url。  该url有效时间10min，超过10min请重新获取。

        :return: The url of this NovaVncConsole.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NovaVncConsole.

        远程登录的url。  该url有效时间10min，超过10min请重新获取。

        :param url: The url of this NovaVncConsole.
        :type: str
        """
        self._url = url

    @property
    def type(self):
        """Gets the type of this NovaVncConsole.

        远程登录的类型。

        :return: The type of this NovaVncConsole.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NovaVncConsole.

        远程登录的类型。

        :param type: The type of this NovaVncConsole.
        :type: str
        """
        self._type = type

    @property
    def protocol(self):
        """Gets the protocol of this NovaVncConsole.

        远程登录的协议。

        :return: The protocol of this NovaVncConsole.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this NovaVncConsole.

        远程登录的协议。

        :param protocol: The protocol of this NovaVncConsole.
        :type: str
        """
        self._protocol = protocol

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
        if not isinstance(other, NovaVncConsole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
