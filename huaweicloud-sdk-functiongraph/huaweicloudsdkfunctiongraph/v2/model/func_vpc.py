# coding: utf-8

import pprint
import re

import six





class FuncVpc:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vpc_name': 'str',
        'vpc_id': 'str',
        'subnet_name': 'str',
        'subnet_id': 'str',
        'cidr': 'str',
        'gateway': 'str'
    }

    attribute_map = {
        'vpc_name': 'vpc_name',
        'vpc_id': 'vpc_id',
        'subnet_name': 'subnet_name',
        'subnet_id': 'subnet_id',
        'cidr': 'cidr',
        'gateway': 'gateway'
    }

    def __init__(self, vpc_name=None, vpc_id=None, subnet_name=None, subnet_id=None, cidr=None, gateway=None):
        """FuncVpc - a model defined in huaweicloud sdk"""
        
        

        self._vpc_name = None
        self._vpc_id = None
        self._subnet_name = None
        self._subnet_id = None
        self._cidr = None
        self._gateway = None
        self.discriminator = None

        self.vpc_name = vpc_name
        self.vpc_id = vpc_id
        self.subnet_name = subnet_name
        self.subnet_id = subnet_id
        self.cidr = cidr
        self.gateway = gateway

    @property
    def vpc_name(self):
        """Gets the vpc_name of this FuncVpc.

        虚拟私有云名称。

        :return: The vpc_name of this FuncVpc.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this FuncVpc.

        虚拟私有云名称。

        :param vpc_name: The vpc_name of this FuncVpc.
        :type: str
        """
        self._vpc_name = vpc_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this FuncVpc.

        虚拟私有云唯一标识。

        :return: The vpc_id of this FuncVpc.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this FuncVpc.

        虚拟私有云唯一标识。

        :param vpc_id: The vpc_id of this FuncVpc.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_name(self):
        """Gets the subnet_name of this FuncVpc.

        子网名称。

        :return: The subnet_name of this FuncVpc.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this FuncVpc.

        子网名称。

        :param subnet_name: The subnet_name of this FuncVpc.
        :type: str
        """
        self._subnet_name = subnet_name

    @property
    def subnet_id(self):
        """Gets the subnet_id of this FuncVpc.

        子网编号。

        :return: The subnet_id of this FuncVpc.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this FuncVpc.

        子网编号。

        :param subnet_id: The subnet_id of this FuncVpc.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def cidr(self):
        """Gets the cidr of this FuncVpc.

        子网掩码。

        :return: The cidr of this FuncVpc.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this FuncVpc.

        子网掩码。

        :param cidr: The cidr of this FuncVpc.
        :type: str
        """
        self._cidr = cidr

    @property
    def gateway(self):
        """Gets the gateway of this FuncVpc.

        网关。

        :return: The gateway of this FuncVpc.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this FuncVpc.

        网关。

        :param gateway: The gateway of this FuncVpc.
        :type: str
        """
        self._gateway = gateway

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
        if not isinstance(other, FuncVpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
