# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMenuRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'menu': 'Menus',
        'change_reason': 'str'
    }

    attribute_map = {
        'menu': 'menu',
        'change_reason': 'change_reason'
    }

    def __init__(self, menu=None, change_reason=None):
        r"""UpdateMenuRequestBody

        The model defined in huaweicloud sdk

        :param menu: 
        :type menu: :class:`huaweicloudsdkkoomessage.v1.Menus`
        :param change_reason: 修改原因。
        :type change_reason: str
        """
        
        

        self._menu = None
        self._change_reason = None
        self.discriminator = None

        self.menu = menu
        self.change_reason = change_reason

    @property
    def menu(self):
        r"""Gets the menu of this UpdateMenuRequestBody.

        :return: The menu of this UpdateMenuRequestBody.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Menus`
        """
        return self._menu

    @menu.setter
    def menu(self, menu):
        r"""Sets the menu of this UpdateMenuRequestBody.

        :param menu: The menu of this UpdateMenuRequestBody.
        :type menu: :class:`huaweicloudsdkkoomessage.v1.Menus`
        """
        self._menu = menu

    @property
    def change_reason(self):
        r"""Gets the change_reason of this UpdateMenuRequestBody.

        修改原因。

        :return: The change_reason of this UpdateMenuRequestBody.
        :rtype: str
        """
        return self._change_reason

    @change_reason.setter
    def change_reason(self, change_reason):
        r"""Sets the change_reason of this UpdateMenuRequestBody.

        修改原因。

        :param change_reason: The change_reason of this UpdateMenuRequestBody.
        :type change_reason: str
        """
        self._change_reason = change_reason

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
        if not isinstance(other, UpdateMenuRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
