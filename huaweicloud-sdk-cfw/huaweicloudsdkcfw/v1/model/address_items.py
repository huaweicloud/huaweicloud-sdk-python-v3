# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddressItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'items': 'list[AddressItemIdWithoutName]',
        'covered_ip': 'list[CoveredIPVO]'
    }

    attribute_map = {
        'items': 'items',
        'covered_ip': 'covered_ip'
    }

    def __init__(self, items=None, covered_ip=None):
        r"""AddressItems

        The model defined in huaweicloud sdk

        :param items: 地址组成员id列表
        :type items: list[:class:`huaweicloudsdkcfw.v1.AddressItemIdWithoutName`]
        :param covered_ip: 覆盖ip列表
        :type covered_ip: list[:class:`huaweicloudsdkcfw.v1.CoveredIPVO`]
        """
        
        

        self._items = None
        self._covered_ip = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if covered_ip is not None:
            self.covered_ip = covered_ip

    @property
    def items(self):
        r"""Gets the items of this AddressItems.

        地址组成员id列表

        :return: The items of this AddressItems.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AddressItemIdWithoutName`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this AddressItems.

        地址组成员id列表

        :param items: The items of this AddressItems.
        :type items: list[:class:`huaweicloudsdkcfw.v1.AddressItemIdWithoutName`]
        """
        self._items = items

    @property
    def covered_ip(self):
        r"""Gets the covered_ip of this AddressItems.

        覆盖ip列表

        :return: The covered_ip of this AddressItems.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.CoveredIPVO`]
        """
        return self._covered_ip

    @covered_ip.setter
    def covered_ip(self, covered_ip):
        r"""Sets the covered_ip of this AddressItems.

        覆盖ip列表

        :param covered_ip: The covered_ip of this AddressItems.
        :type covered_ip: list[:class:`huaweicloudsdkcfw.v1.CoveredIPVO`]
        """
        self._covered_ip = covered_ip

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
        if not isinstance(other, AddressItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
