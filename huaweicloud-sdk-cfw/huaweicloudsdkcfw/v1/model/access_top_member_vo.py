# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessTopMemberVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'str',
        'item': 'str',
        'name': 'str'
    }

    attribute_map = {
        'count': 'count',
        'item': 'item',
        'name': 'name'
    }

    def __init__(self, count=None, item=None, name=None):
        r"""AccessTopMemberVO

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 次数 **取值范围**： 不涉及
        :type count: str
        :param item: **参数解释**： 项 **取值范围**： 不涉及
        :type item: str
        :param name: **参数解释**： 项名称 **取值范围**： 不涉及
        :type name: str
        """
        
        

        self._count = None
        self._item = None
        self._name = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if item is not None:
            self.item = item
        if name is not None:
            self.name = name

    @property
    def count(self):
        r"""Gets the count of this AccessTopMemberVO.

        **参数解释**： 次数 **取值范围**： 不涉及

        :return: The count of this AccessTopMemberVO.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this AccessTopMemberVO.

        **参数解释**： 次数 **取值范围**： 不涉及

        :param count: The count of this AccessTopMemberVO.
        :type count: str
        """
        self._count = count

    @property
    def item(self):
        r"""Gets the item of this AccessTopMemberVO.

        **参数解释**： 项 **取值范围**： 不涉及

        :return: The item of this AccessTopMemberVO.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this AccessTopMemberVO.

        **参数解释**： 项 **取值范围**： 不涉及

        :param item: The item of this AccessTopMemberVO.
        :type item: str
        """
        self._item = item

    @property
    def name(self):
        r"""Gets the name of this AccessTopMemberVO.

        **参数解释**： 项名称 **取值范围**： 不涉及

        :return: The name of this AccessTopMemberVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AccessTopMemberVO.

        **参数解释**： 项名称 **取值范围**： 不涉及

        :param name: The name of this AccessTopMemberVO.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AccessTopMemberVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
