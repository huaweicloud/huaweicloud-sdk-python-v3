# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionItemVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_name': 'str',
        'sub_items': 'list[ActionSubItemVo]'
    }

    attribute_map = {
        'item_name': 'item_name',
        'sub_items': 'sub_items'
    }

    def __init__(self, item_name=None, sub_items=None):
        r"""ActionItemVo

        The model defined in huaweicloud sdk

        :param item_name: **参数解释**： 任务详情子项，一级菜单。 **取值范围**： 不涉及。
        :type item_name: str
        :param sub_items: **参数解释**： 任务详情子项，一级菜单详情。 **取值范围**： 不涉及。
        :type sub_items: list[:class:`huaweicloudsdkdws.v2.ActionSubItemVo`]
        """
        
        

        self._item_name = None
        self._sub_items = None
        self.discriminator = None

        if item_name is not None:
            self.item_name = item_name
        if sub_items is not None:
            self.sub_items = sub_items

    @property
    def item_name(self):
        r"""Gets the item_name of this ActionItemVo.

        **参数解释**： 任务详情子项，一级菜单。 **取值范围**： 不涉及。

        :return: The item_name of this ActionItemVo.
        :rtype: str
        """
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        r"""Sets the item_name of this ActionItemVo.

        **参数解释**： 任务详情子项，一级菜单。 **取值范围**： 不涉及。

        :param item_name: The item_name of this ActionItemVo.
        :type item_name: str
        """
        self._item_name = item_name

    @property
    def sub_items(self):
        r"""Gets the sub_items of this ActionItemVo.

        **参数解释**： 任务详情子项，一级菜单详情。 **取值范围**： 不涉及。

        :return: The sub_items of this ActionItemVo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ActionSubItemVo`]
        """
        return self._sub_items

    @sub_items.setter
    def sub_items(self, sub_items):
        r"""Sets the sub_items of this ActionItemVo.

        **参数解释**： 任务详情子项，一级菜单详情。 **取值范围**： 不涉及。

        :param sub_items: The sub_items of this ActionItemVo.
        :type sub_items: list[:class:`huaweicloudsdkdws.v2.ActionSubItemVo`]
        """
        self._sub_items = sub_items

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
        if not isinstance(other, ActionItemVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
