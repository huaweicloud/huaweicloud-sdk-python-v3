# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Menus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'menu_items': 'list[MenuItem]'
    }

    attribute_map = {
        'menu_items': 'menu_items'
    }

    def __init__(self, menu_items=None):
        r"""Menus

        The model defined in huaweicloud sdk

        :param menu_items: 各子菜单项配置。 
        :type menu_items: list[:class:`huaweicloudsdkkoomessage.v1.MenuItem`]
        """
        
        

        self._menu_items = None
        self.discriminator = None

        self.menu_items = menu_items

    @property
    def menu_items(self):
        r"""Gets the menu_items of this Menus.

        各子菜单项配置。 

        :return: The menu_items of this Menus.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.MenuItem`]
        """
        return self._menu_items

    @menu_items.setter
    def menu_items(self, menu_items):
        r"""Sets the menu_items of this Menus.

        各子菜单项配置。 

        :param menu_items: The menu_items of this Menus.
        :type menu_items: list[:class:`huaweicloudsdkkoomessage.v1.MenuItem`]
        """
        self._menu_items = menu_items

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
        if not isinstance(other, Menus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
