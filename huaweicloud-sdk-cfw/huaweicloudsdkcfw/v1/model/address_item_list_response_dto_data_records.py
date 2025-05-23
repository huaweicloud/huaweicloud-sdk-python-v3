# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressItemListResponseDTODataRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_id': 'str',
        'name': 'str',
        'description': 'str',
        'address_type': 'int',
        'address': 'str'
    }

    attribute_map = {
        'item_id': 'item_id',
        'name': 'name',
        'description': 'description',
        'address_type': 'address_type',
        'address': 'address'
    }

    def __init__(self, item_id=None, name=None, description=None, address_type=None, address=None):
        r"""AddressItemListResponseDTODataRecords

        The model defined in huaweicloud sdk

        :param item_id: 地址组成员id
        :type item_id: str
        :param name: 地址组成员name
        :type name: str
        :param description: 描述
        :type description: str
        :param address_type: 地址组类型，0 ipv4,1 ipv6
        :type address_type: int
        :param address: 地址信息
        :type address: str
        """
        
        

        self._item_id = None
        self._name = None
        self._description = None
        self._address_type = None
        self._address = None
        self.discriminator = None

        if item_id is not None:
            self.item_id = item_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if address_type is not None:
            self.address_type = address_type
        if address is not None:
            self.address = address

    @property
    def item_id(self):
        r"""Gets the item_id of this AddressItemListResponseDTODataRecords.

        地址组成员id

        :return: The item_id of this AddressItemListResponseDTODataRecords.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this AddressItemListResponseDTODataRecords.

        地址组成员id

        :param item_id: The item_id of this AddressItemListResponseDTODataRecords.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def name(self):
        r"""Gets the name of this AddressItemListResponseDTODataRecords.

        地址组成员name

        :return: The name of this AddressItemListResponseDTODataRecords.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddressItemListResponseDTODataRecords.

        地址组成员name

        :param name: The name of this AddressItemListResponseDTODataRecords.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AddressItemListResponseDTODataRecords.

        描述

        :return: The description of this AddressItemListResponseDTODataRecords.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AddressItemListResponseDTODataRecords.

        描述

        :param description: The description of this AddressItemListResponseDTODataRecords.
        :type description: str
        """
        self._description = description

    @property
    def address_type(self):
        r"""Gets the address_type of this AddressItemListResponseDTODataRecords.

        地址组类型，0 ipv4,1 ipv6

        :return: The address_type of this AddressItemListResponseDTODataRecords.
        :rtype: int
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        r"""Sets the address_type of this AddressItemListResponseDTODataRecords.

        地址组类型，0 ipv4,1 ipv6

        :param address_type: The address_type of this AddressItemListResponseDTODataRecords.
        :type address_type: int
        """
        self._address_type = address_type

    @property
    def address(self):
        r"""Gets the address of this AddressItemListResponseDTODataRecords.

        地址信息

        :return: The address of this AddressItemListResponseDTODataRecords.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this AddressItemListResponseDTODataRecords.

        地址信息

        :param address: The address of this AddressItemListResponseDTODataRecords.
        :type address: str
        """
        self._address = address

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
        if not isinstance(other, AddressItemListResponseDTODataRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
