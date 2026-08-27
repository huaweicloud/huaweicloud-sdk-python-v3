# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PayloadObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'list': 'list[object]',
        'page_info': 'PageInfo',
        'item': 'object'
    }

    attribute_map = {
        'list': 'list',
        'page_info': 'page_info',
        'item': 'item'
    }

    def __init__(self, list=None, page_info=None, item=None):
        r"""PayloadObject

        The model defined in huaweicloud sdk

        :param list: **参数解释**： 返回信息列表。 **约束限制**： 不涉及 **取值范围**： 元素数量范围[0,100000000]。 **默认取值**： 不涉及 
        :type list: list[object]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkoptverse.v1.PageInfo`
        :param item: **参数解释**： 返回对象信息。 **约束限制**： 不涉及 **取值范围**： 不涉及。 **默认取值**： 不涉及 
        :type item: object
        """
        
        

        self._list = None
        self._page_info = None
        self._item = None
        self.discriminator = None

        if list is not None:
            self.list = list
        if page_info is not None:
            self.page_info = page_info
        if item is not None:
            self.item = item

    @property
    def list(self):
        r"""Gets the list of this PayloadObject.

        **参数解释**： 返回信息列表。 **约束限制**： 不涉及 **取值范围**： 元素数量范围[0,100000000]。 **默认取值**： 不涉及 

        :return: The list of this PayloadObject.
        :rtype: list[object]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this PayloadObject.

        **参数解释**： 返回信息列表。 **约束限制**： 不涉及 **取值范围**： 元素数量范围[0,100000000]。 **默认取值**： 不涉及 

        :param list: The list of this PayloadObject.
        :type list: list[object]
        """
        self._list = list

    @property
    def page_info(self):
        r"""Gets the page_info of this PayloadObject.

        :return: The page_info of this PayloadObject.
        :rtype: :class:`huaweicloudsdkoptverse.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this PayloadObject.

        :param page_info: The page_info of this PayloadObject.
        :type page_info: :class:`huaweicloudsdkoptverse.v1.PageInfo`
        """
        self._page_info = page_info

    @property
    def item(self):
        r"""Gets the item of this PayloadObject.

        **参数解释**： 返回对象信息。 **约束限制**： 不涉及 **取值范围**： 不涉及。 **默认取值**： 不涉及 

        :return: The item of this PayloadObject.
        :rtype: object
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this PayloadObject.

        **参数解释**： 返回对象信息。 **约束限制**： 不涉及 **取值范围**： 不涉及。 **默认取值**： 不涉及 

        :param item: The item of this PayloadObject.
        :type item: object
        """
        self._item = item

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayloadObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
