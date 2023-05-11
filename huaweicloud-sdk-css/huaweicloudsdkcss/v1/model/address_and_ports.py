# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressAndPorts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'port': 'int'
    }

    attribute_map = {
        'address': 'address',
        'port': 'port'
    }

    def __init__(self, address=None, port=None):
        """AddressAndPorts

        The model defined in huaweicloud sdk

        :param address: IP地址或域名。
        :type address: str
        :param port: 端口号。
        :type port: int
        """
        
        

        self._address = None
        self._port = None
        self.discriminator = None

        self.address = address
        if port is not None:
            self.port = port

    @property
    def address(self):
        """Gets the address of this AddressAndPorts.

        IP地址或域名。

        :return: The address of this AddressAndPorts.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AddressAndPorts.

        IP地址或域名。

        :param address: The address of this AddressAndPorts.
        :type address: str
        """
        self._address = address

    @property
    def port(self):
        """Gets the port of this AddressAndPorts.

        端口号。

        :return: The port of this AddressAndPorts.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this AddressAndPorts.

        端口号。

        :param port: The port of this AddressAndPorts.
        :type port: int
        """
        self._port = port

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
        if not isinstance(other, AddressAndPorts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
