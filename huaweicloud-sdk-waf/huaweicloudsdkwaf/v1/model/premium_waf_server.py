# coding: utf-8

import pprint
import re

import six





class PremiumWafServer:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'front_protocol': 'str',
        'back_protocol': 'str',
        'address': 'str',
        'port': 'int',
        'type': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'front_protocol': 'front_protocol',
        'back_protocol': 'back_protocol',
        'address': 'address',
        'port': 'port',
        'type': 'type',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, front_protocol=None, back_protocol=None, address=None, port=None, type=None, vpc_id=None):
        """PremiumWafServer - a model defined in huaweicloud sdk"""
        
        

        self._front_protocol = None
        self._back_protocol = None
        self._address = None
        self._port = None
        self._type = None
        self._vpc_id = None
        self.discriminator = None

        self.front_protocol = front_protocol
        self.back_protocol = back_protocol
        self.address = address
        self.port = port
        if type is not None:
            self.type = type
        if vpc_id is not None:
            self.vpc_id = vpc_id

    @property
    def front_protocol(self):
        """Gets the front_protocol of this PremiumWafServer.

        对外协议

        :return: The front_protocol of this PremiumWafServer.
        :rtype: str
        """
        return self._front_protocol

    @front_protocol.setter
    def front_protocol(self, front_protocol):
        """Sets the front_protocol of this PremiumWafServer.

        对外协议

        :param front_protocol: The front_protocol of this PremiumWafServer.
        :type: str
        """
        self._front_protocol = front_protocol

    @property
    def back_protocol(self):
        """Gets the back_protocol of this PremiumWafServer.

        源站协议

        :return: The back_protocol of this PremiumWafServer.
        :rtype: str
        """
        return self._back_protocol

    @back_protocol.setter
    def back_protocol(self, back_protocol):
        """Sets the back_protocol of this PremiumWafServer.

        源站协议

        :param back_protocol: The back_protocol of this PremiumWafServer.
        :type: str
        """
        self._back_protocol = back_protocol

    @property
    def address(self):
        """Gets the address of this PremiumWafServer.

        源站地址

        :return: The address of this PremiumWafServer.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PremiumWafServer.

        源站地址

        :param address: The address of this PremiumWafServer.
        :type: str
        """
        self._address = address

    @property
    def port(self):
        """Gets the port of this PremiumWafServer.

        源站端口

        :return: The port of this PremiumWafServer.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PremiumWafServer.

        源站端口

        :param port: The port of this PremiumWafServer.
        :type: int
        """
        self._port = port

    @property
    def type(self):
        """Gets the type of this PremiumWafServer.

        源站地址为ipv4或ipv6

        :return: The type of this PremiumWafServer.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PremiumWafServer.

        源站地址为ipv4或ipv6

        :param type: The type of this PremiumWafServer.
        :type: str
        """
        self._type = type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this PremiumWafServer.

        源站所在VPC ID

        :return: The vpc_id of this PremiumWafServer.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this PremiumWafServer.

        源站所在VPC ID

        :param vpc_id: The vpc_id of this PremiumWafServer.
        :type: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, PremiumWafServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other