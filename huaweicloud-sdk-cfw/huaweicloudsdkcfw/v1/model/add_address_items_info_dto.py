# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddAddressItemsInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'address_items': 'list[AddAddressItemsInfoDtoAddressItems]'
    }

    attribute_map = {
        'set_id': 'set_id',
        'address_items': 'address_items'
    }

    def __init__(self, set_id=None, address_items=None):
        """AddAddressItemsInfoDto

        The model defined in huaweicloud sdk

        :param set_id: 地址组id
        :type set_id: str
        :param address_items: 地址组成员信息
        :type address_items: list[:class:`huaweicloudsdkcfw.v1.AddAddressItemsInfoDtoAddressItems`]
        """
        
        

        self._set_id = None
        self._address_items = None
        self.discriminator = None

        if set_id is not None:
            self.set_id = set_id
        if address_items is not None:
            self.address_items = address_items

    @property
    def set_id(self):
        """Gets the set_id of this AddAddressItemsInfoDto.

        地址组id

        :return: The set_id of this AddAddressItemsInfoDto.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this AddAddressItemsInfoDto.

        地址组id

        :param set_id: The set_id of this AddAddressItemsInfoDto.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def address_items(self):
        """Gets the address_items of this AddAddressItemsInfoDto.

        地址组成员信息

        :return: The address_items of this AddAddressItemsInfoDto.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AddAddressItemsInfoDtoAddressItems`]
        """
        return self._address_items

    @address_items.setter
    def address_items(self, address_items):
        """Sets the address_items of this AddAddressItemsInfoDto.

        地址组成员信息

        :param address_items: The address_items of this AddAddressItemsInfoDto.
        :type address_items: list[:class:`huaweicloudsdkcfw.v1.AddAddressItemsInfoDtoAddressItems`]
        """
        self._address_items = address_items

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
        if not isinstance(other, AddAddressItemsInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
