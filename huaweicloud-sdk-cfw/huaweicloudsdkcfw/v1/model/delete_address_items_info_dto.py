# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAddressItemsInfoDto:

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
        'address_item_ids': 'list[str]'
    }

    attribute_map = {
        'set_id': 'set_id',
        'address_item_ids': 'address_item_ids'
    }

    def __init__(self, set_id=None, address_item_ids=None):
        r"""DeleteAddressItemsInfoDto

        The model defined in huaweicloud sdk

        :param set_id: 地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。
        :type set_id: str
        :param address_item_ids: 地址组成员id列表，地址组成员id可通过[查询地址组成员接口](ListAddressItems.xml)查询获得，通过返回值中的data.records.item_id（.表示各对象之间层级的区分）获得。
        :type address_item_ids: list[str]
        """
        
        

        self._set_id = None
        self._address_item_ids = None
        self.discriminator = None

        self.set_id = set_id
        self.address_item_ids = address_item_ids

    @property
    def set_id(self):
        r"""Gets the set_id of this DeleteAddressItemsInfoDto.

        地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :return: The set_id of this DeleteAddressItemsInfoDto.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        r"""Sets the set_id of this DeleteAddressItemsInfoDto.

        地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :param set_id: The set_id of this DeleteAddressItemsInfoDto.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def address_item_ids(self):
        r"""Gets the address_item_ids of this DeleteAddressItemsInfoDto.

        地址组成员id列表，地址组成员id可通过[查询地址组成员接口](ListAddressItems.xml)查询获得，通过返回值中的data.records.item_id（.表示各对象之间层级的区分）获得。

        :return: The address_item_ids of this DeleteAddressItemsInfoDto.
        :rtype: list[str]
        """
        return self._address_item_ids

    @address_item_ids.setter
    def address_item_ids(self, address_item_ids):
        r"""Sets the address_item_ids of this DeleteAddressItemsInfoDto.

        地址组成员id列表，地址组成员id可通过[查询地址组成员接口](ListAddressItems.xml)查询获得，通过返回值中的data.records.item_id（.表示各对象之间层级的区分）获得。

        :param address_item_ids: The address_item_ids of this DeleteAddressItemsInfoDto.
        :type address_item_ids: list[str]
        """
        self._address_item_ids = address_item_ids

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
        if not isinstance(other, DeleteAddressItemsInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
