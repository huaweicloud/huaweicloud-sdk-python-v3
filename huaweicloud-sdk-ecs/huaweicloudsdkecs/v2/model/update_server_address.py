# coding: utf-8

import pprint
import re

import six





class UpdateServerAddress:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'version': 'int',
        'addr': 'str'
    }

    attribute_map = {
        'version': 'version',
        'addr': 'addr'
    }

    def __init__(self, version=None, addr=None):
        """UpdateServerAddress - a model defined in huaweicloud sdk"""
        
        

        self._version = None
        self._addr = None
        self.discriminator = None

        self.version = version
        self.addr = addr

    @property
    def version(self):
        """Gets the version of this UpdateServerAddress.

        IP地址版本。  - 4：代表IPv4。 - 6：代表IPv6。

        :return: The version of this UpdateServerAddress.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateServerAddress.

        IP地址版本。  - 4：代表IPv4。 - 6：代表IPv6。

        :param version: The version of this UpdateServerAddress.
        :type: int
        """
        self._version = version

    @property
    def addr(self):
        """Gets the addr of this UpdateServerAddress.

        IP地址。

        :return: The addr of this UpdateServerAddress.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this UpdateServerAddress.

        IP地址。

        :param addr: The addr of this UpdateServerAddress.
        :type: str
        """
        self._addr = addr

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
        if not isinstance(other, UpdateServerAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
