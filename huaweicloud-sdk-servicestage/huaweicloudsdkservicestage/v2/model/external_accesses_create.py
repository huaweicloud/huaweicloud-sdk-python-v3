# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExternalAccessesCreate:

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
        'address': 'str',
        'forward_port': 'int'
    }

    attribute_map = {
        'protocol': 'protocol',
        'address': 'address',
        'forward_port': 'forward_port'
    }

    def __init__(self, protocol=None, address=None, forward_port=None):
        """ExternalAccessesCreate

        The model defined in huaweicloud sdk

        :param protocol: 协议，支持http、https。
        :type protocol: str
        :param address: 访问地址。
        :type address: str
        :param forward_port: 端口号。
        :type forward_port: int
        """
        
        

        self._protocol = None
        self._address = None
        self._forward_port = None
        self.discriminator = None

        self.protocol = protocol
        self.address = address
        self.forward_port = forward_port

    @property
    def protocol(self):
        """Gets the protocol of this ExternalAccessesCreate.

        协议，支持http、https。

        :return: The protocol of this ExternalAccessesCreate.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ExternalAccessesCreate.

        协议，支持http、https。

        :param protocol: The protocol of this ExternalAccessesCreate.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def address(self):
        """Gets the address of this ExternalAccessesCreate.

        访问地址。

        :return: The address of this ExternalAccessesCreate.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ExternalAccessesCreate.

        访问地址。

        :param address: The address of this ExternalAccessesCreate.
        :type address: str
        """
        self._address = address

    @property
    def forward_port(self):
        """Gets the forward_port of this ExternalAccessesCreate.

        端口号。

        :return: The forward_port of this ExternalAccessesCreate.
        :rtype: int
        """
        return self._forward_port

    @forward_port.setter
    def forward_port(self, forward_port):
        """Sets the forward_port of this ExternalAccessesCreate.

        端口号。

        :param forward_port: The forward_port of this ExternalAccessesCreate.
        :type forward_port: int
        """
        self._forward_port = forward_port

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
        if not isinstance(other, ExternalAccessesCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
