# coding: utf-8

import pprint
import re

import six





class AllowAddressNetmasksOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'address_netmask': 'str',
        'description': 'str'
    }

    attribute_map = {
        'address_netmask': 'address_netmask',
        'description': 'description'
    }

    def __init__(self, address_netmask=None, description=None):
        """AllowAddressNetmasksOption - a model defined in huaweicloud sdk"""
        
        

        self._address_netmask = None
        self._description = None
        self.discriminator = None

        self.address_netmask = address_netmask
        if description is not None:
            self.description = description

    @property
    def address_netmask(self):
        """Gets the address_netmask of this AllowAddressNetmasksOption.

        IP地址或网段,例如:192.168.0.1/24。

        :return: The address_netmask of this AllowAddressNetmasksOption.
        :rtype: str
        """
        return self._address_netmask

    @address_netmask.setter
    def address_netmask(self, address_netmask):
        """Sets the address_netmask of this AllowAddressNetmasksOption.

        IP地址或网段,例如:192.168.0.1/24。

        :param address_netmask: The address_netmask of this AllowAddressNetmasksOption.
        :type: str
        """
        self._address_netmask = address_netmask

    @property
    def description(self):
        """Gets the description of this AllowAddressNetmasksOption.

        描述信息。

        :return: The description of this AllowAddressNetmasksOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AllowAddressNetmasksOption.

        描述信息。

        :param description: The description of this AllowAddressNetmasksOption.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, AllowAddressNetmasksOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
