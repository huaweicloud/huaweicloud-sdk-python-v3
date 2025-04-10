# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddAddressItemsInfoDtoAddressItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address_type': 'int',
        'address': 'str',
        'description': 'str'
    }

    attribute_map = {
        'address_type': 'address_type',
        'address': 'address',
        'description': 'description'
    }

    def __init__(self, address_type=None, address=None, description=None):
        r"""AddAddressItemsInfoDtoAddressItems

        The model defined in huaweicloud sdk

        :param address_type: 地址类型0 ipv4，1 ipv6
        :type address_type: int
        :param address: ip
        :type address: str
        :param description: 地址组成员描述
        :type description: str
        """
        
        

        self._address_type = None
        self._address = None
        self._description = None
        self.discriminator = None

        if address_type is not None:
            self.address_type = address_type
        self.address = address
        if description is not None:
            self.description = description

    @property
    def address_type(self):
        r"""Gets the address_type of this AddAddressItemsInfoDtoAddressItems.

        地址类型0 ipv4，1 ipv6

        :return: The address_type of this AddAddressItemsInfoDtoAddressItems.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this AddAddressItemsInfoDtoAddressItems.

        地址类型0 ipv4，1 ipv6

        :param address_type: The address_type of this AddAddressItemsInfoDtoAddressItems.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        r"""Gets the address of this AddAddressItemsInfoDtoAddressItems.

        ip

        :return: The address of this AddAddressItemsInfoDtoAddressItems.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this AddAddressItemsInfoDtoAddressItems.

        ip

        :param address: The address of this AddAddressItemsInfoDtoAddressItems.
        :type address: str
        """
        self._address = address

    @property
    def description(self):
        r"""Gets the description of this AddAddressItemsInfoDtoAddressItems.

        地址组成员描述

        :return: The description of this AddAddressItemsInfoDtoAddressItems.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddAddressItemsInfoDtoAddressItems.

        地址组成员描述

        :param description: The description of this AddAddressItemsInfoDtoAddressItems.
        :type description: str
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
        if not isinstance(other, AddAddressItemsInfoDtoAddressItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
