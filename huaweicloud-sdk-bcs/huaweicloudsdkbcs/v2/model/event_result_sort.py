# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventResultSort:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_by': 'list[str]',
        'order': 'str'
    }

    attribute_map = {
        'order_by': 'order_by',
        'order': 'order'
    }

    def __init__(self, order_by=None, order=None):
        r"""EventResultSort

        The model defined in huaweicloud sdk

        :param order_by: 排序字段列表。会根据列表中定义顺序对返回列表最排序
        :type order_by: list[str]
        :param order: 排序方式枚举值。asc代表正序，desc代表倒序
        :type order: str
        """
        
        

        self._order_by = None
        self._order = None
        self.discriminator = None

        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order

    @property
    def order_by(self):
        r"""Gets the order_by of this EventResultSort.

        排序字段列表。会根据列表中定义顺序对返回列表最排序

        :return: The order_by of this EventResultSort.
        :rtype: list[str]
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this EventResultSort.

        排序字段列表。会根据列表中定义顺序对返回列表最排序

        :param order_by: The order_by of this EventResultSort.
        :type order_by: list[str]
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this EventResultSort.

        排序方式枚举值。asc代表正序，desc代表倒序

        :return: The order of this EventResultSort.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this EventResultSort.

        排序方式枚举值。asc代表正序，desc代表倒序

        :param order: The order of this EventResultSort.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, EventResultSort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
