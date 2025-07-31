# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'item': 'str',
        'item_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'item': 'item',
        'item_id': 'item_id'
    }

    def __init__(self, count=None, item=None, item_id=None):
        r"""TopInfo

        The model defined in huaweicloud sdk

        :param count: **参数解释**： 次数 **取值范围**： 不涉及
        :type count: int
        :param item: **参数解释**： 项 **取值范围**： 不涉及
        :type item: str
        :param item_id: **参数解释**： 项ID **取值范围**： 不涉及
        :type item_id: str
        """
        
        

        self._count = None
        self._item = None
        self._item_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if item is not None:
            self.item = item
        if item_id is not None:
            self.item_id = item_id

    @property
    def count(self):
        r"""Gets the count of this TopInfo.

        **参数解释**： 次数 **取值范围**： 不涉及

        :return: The count of this TopInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this TopInfo.

        **参数解释**： 次数 **取值范围**： 不涉及

        :param count: The count of this TopInfo.
        :type count: int
        """
        self._count = count

    @property
    def item(self):
        r"""Gets the item of this TopInfo.

        **参数解释**： 项 **取值范围**： 不涉及

        :return: The item of this TopInfo.
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        r"""Sets the item of this TopInfo.

        **参数解释**： 项 **取值范围**： 不涉及

        :param item: The item of this TopInfo.
        :type item: str
        """
        self._item = item

    @property
    def item_id(self):
        r"""Gets the item_id of this TopInfo.

        **参数解释**： 项ID **取值范围**： 不涉及

        :return: The item_id of this TopInfo.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this TopInfo.

        **参数解释**： 项ID **取值范围**： 不涉及

        :param item_id: The item_id of this TopInfo.
        :type item_id: str
        """
        self._item_id = item_id

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
        if not isinstance(other, TopInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
